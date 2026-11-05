const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require('@playwright/test');

const PORT = 4174;
const BASE_URL = `http://localhost:${PORT}`;
const ROOT_DIR = path.resolve(__dirname, '..');

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.webp': 'image/webp',
  '.mp4': 'video/mp4',
  '.vtt': 'text/vtt; charset=utf-8',
  '.xml': 'application/xml; charset=utf-8',
  '.txt': 'text/plain; charset=utf-8'
};

function createServer() {
  return http.createServer((req, res) => {
    let reqPath = decodeURI(req.url.split('?')[0]);
    if (reqPath.endsWith('/')) {
      reqPath += 'index.html';
    }

    let filePath = path.join(ROOT_DIR, reqPath);
    if (!fs.existsSync(filePath)) {
      res.writeHead(404, { 'Content-Type': 'text/plain', 'Connection': 'close' });
      res.end('404 Not Found: ' + reqPath);
      return;
    }

    if (fs.statSync(filePath).isDirectory()) {
      filePath = path.join(filePath, 'index.html');
      if (!fs.existsSync(filePath)) {
        res.writeHead(404, { 'Content-Type': 'text/plain', 'Connection': 'close' });
        res.end('404 Not Found');
        return;
      }
    }

    const ext = path.extname(filePath).toLowerCase();
    const contentType = MIME_TYPES[ext] || 'application/octet-stream';
    const stat = fs.statSync(filePath);

    res.writeHead(200, {
      'Content-Type': contentType,
      'Content-Length': stat.size,
      'Accept-Ranges': 'bytes'
    });

    const readStream = fs.createReadStream(filePath);
    readStream.on('error', () => {
      if (!res.headersSent) res.writeHead(500);
      res.end();
    });
    readStream.pipe(res);
  });
}

async function auditPage(page, urlPath) {
  await page.goto(`${BASE_URL}${urlPath}`, { waitUntil: 'domcontentloaded', timeout: 15000 });
  await page.waitForTimeout(1000);

  const metrics = await page.evaluate(async () => {
    // Navigation timing
    const navEntries = performance.getEntriesByType('navigation');
    const nav = navEntries.length > 0 ? navEntries[0] : null;

    // Paint timing
    const paintEntries = performance.getEntriesByType('paint');
    let fcp = 0;
    paintEntries.forEach(entry => {
      if (entry.name === 'first-contentful-paint') {
        fcp = entry.startTime;
      }
    });

    // DOM metrics
    const totalElements = document.getElementsByTagName('*').length;
    const scriptsCount = document.getElementsByTagName('script').length;
    const stylesCount = document.getElementsByTagName('link').length;
    const imagesCount = document.getElementsByTagName('img').length;

    // A11y basics
    const imagesMissingAlt = Array.from(document.querySelectorAll('img')).filter(img => !img.hasAttribute('alt')).length;
    const headingLevels = Array.from(document.querySelectorAll('h1, h2, h3, h4, h5, h6')).map(h => h.tagName);

    return {
      fcp: Math.round(fcp),
      domContentLoaded: nav ? Math.round(nav.domContentLoadedEventEnd - nav.startTime) : 0,
      loadEvent: nav ? Math.round(nav.loadEventEnd - nav.startTime) : 0,
      totalElements,
      scriptsCount,
      stylesCount,
      imagesCount,
      imagesMissingAlt,
      headingLevels: headingLevels.slice(0, 8)
    };
  });

  return metrics;
}

async function run() {
  const server = createServer();
  await new Promise(resolve => server.listen(PORT, resolve));

  const browser = await chromium.launch({
    channel: 'chrome',
    headless: true
  });

  const pages = [
    { name: 'Homepage', path: '/' },
    { name: 'Interactive Estimator', path: '/estimate/' },
    { name: 'Featured Work Portfolio', path: '/work/' },
    { name: 'Consultation & Contact', path: '/contact/' },
    { name: 'Ecosystem & Video', path: '/ecosystem/' }
  ];

  console.log('='.repeat(90));
  console.log('VALIXIS TECHNOLOGIES — CORE WEB VITALS & RUNTIME PERFORMANCE AUDIT');
  console.log('='.repeat(90));

  try {
    const page = await browser.newPage({
      viewport: { width: 1440, height: 900 }
    });

    for (const p of pages) {
      const m = await auditPage(page, p.path);
      console.log(`\nPage: ${p.name} (${p.path})`);
      console.log(`  - First Contentful Paint (FCP): ${m.fcp} ms`);
      console.log(`  - DOM Content Loaded:          ${m.domContentLoaded} ms`);
      console.log(`  - Total DOM Elements:           ${m.totalElements}`);
      console.log(`  - Images without alt text:      ${m.imagesMissingAlt} (0 expected)`);
      console.log(`  - Headings sequence:            ${m.headingLevels.join(' > ')}`);
    }

  } finally {
    await browser.close();
    try { if (server.closeAllConnections) server.closeAllConnections(); } catch (e) {}
    try { server.close(); } catch (e) {}
  }
}

run().catch(err => {
  console.error('Audit error:', err);
  process.exit(1);
});
