const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require('@playwright/test');

const PORT = 4190;
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
  '.ico': 'image/x-icon',
  '.txt': 'text/plain; charset=utf-8',
  '.xml': 'application/xml; charset=utf-8'
};

function createServer() {
  return http.createServer((req, res) => {
    let reqPath = decodeURI(req.url.split('?')[0]);
    if (reqPath.endsWith('/')) reqPath += 'index.html';

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
    readStream.pipe(res);
  });
}

const PAGES_TO_TEST = [
  '/',
  '/about/',
  '/services/',
  '/services/ai-automation/',
  '/services/software-mobile/',
  '/services/web-platforms/',
  '/services/3d-gaming-interactive/',
  '/ecosystem/',
  '/estimate/',
  '/contact/',
  '/privacy/',
  '/client-sites/'
];

const VIEWPORTS = [
  { name: 'Mobile-Small (360x740)', width: 360, height: 740 },
  { name: 'Mobile-iPhone (390x844)', width: 390, height: 844 },
  { name: 'Tablet-iPad (768x1024)', width: 768, height: 1024 },
  { name: 'Desktop-Large (1440x900)', width: 1440, height: 900 }
];

async function runBugHunt() {
  const server = createServer();
  await new Promise(resolve => server.listen(PORT, resolve));
  console.log(`\n============================================================`);
  console.log(`VALIXIS DEEP AUTOMATED BUG HUNT`);
  console.log(`Local test server running at ${BASE_URL}`);
  console.log(`============================================================\n`);

  const browser = await chromium.launch({
    channel: 'chrome',
    headless: true
  });

  const findings = [];
  function reportBug(severity, category, pageUrl, description) {
    findings.push({ severity, category, pageUrl, description });
    console.log(`[${severity}] [${category}] ${pageUrl}: ${description}`);
  }

  try {
    for (const pagePath of PAGES_TO_TEST) {
      console.log(`\n>>> Auditing Page: ${pagePath} ...`);
      const context = await browser.newContext({
        viewport: { width: 1440, height: 900 }
      });
      const page = await context.newPage();

      const failedRequests = [];
      page.on('requestfailed', req => {
        // Ignore Google AdSense, third party ads, or analytics if network offline
        const url = req.url();
        if (!url.includes('google') && !url.includes('doubleclick') && !url.includes('abscloud') && !url.includes('bauval')) {
          failedRequests.push({ url, failure: req.failure() ? req.failure().errorText : 'failed' });
        }
      });

      page.on('response', resp => {
        if (resp.status() >= 400 && resp.url().startsWith(BASE_URL)) {
          failedRequests.push({ url: resp.url(), status: resp.status() });
        }
      });

      const consoleErrors = [];
      page.on('console', msg => {
        if (msg.type() === 'error') {
          const txt = msg.text();
          // Filter known third-party tracker/adblock blocks
          if (!txt.includes('ERR_BLOCKED_BY_CLIENT') && !txt.includes('google') && !txt.includes('adsbygoogle')) {
            consoleErrors.push(txt);
          }
        }
      });
      page.on('pageerror', err => consoleErrors.push(err.message));

      // 1. Load Page
      try {
        await page.goto(`${BASE_URL}${pagePath}`, { waitUntil: 'domcontentloaded', timeout: 12000 });
        await page.waitForTimeout(1500);
      } catch (err) {
        reportBug('CRITICAL', 'Page Load', pagePath, `Page failed to load: ${err.message}`);
        await context.close();
        continue;
      }

      // Check Console & Failed requests
      if (consoleErrors.length > 0) {
        consoleErrors.forEach(err => reportBug('HIGH', 'Console Error', pagePath, err));
      }
      if (failedRequests.length > 0) {
        failedRequests.forEach(req => reportBug('HIGH', 'Broken Asset / 404', pagePath, `${req.url} (${req.status || req.failure})`));
      }

      // 2. Check for Broken Images
      const brokenImages = await page.evaluate(() => {
        const imgs = Array.from(document.querySelectorAll('img'));
        const bad = [];
        for (const img of imgs) {
          if (!img.src || img.naturalWidth === 0) {
            bad.push(img.src || img.getAttribute('src') || '<no src>');
          }
        }
        return bad;
      });
      if (brokenImages.length > 0) {
        brokenImages.forEach(src => reportBug('HIGH', 'Broken Image', pagePath, `Image failed to render (naturalWidth=0): ${src}`));
      }

      // 3. Check for Stuck / Invisible Core Elements
      // Scroll down and wait for transition (650ms) to ensure reveals execute cleanly
      await page.evaluate(() => {
        window.scrollTo(0, document.body.scrollHeight / 2);
      });
      await page.waitForTimeout(400);
      await page.evaluate(() => {
        window.scrollTo(0, document.body.scrollHeight);
      });
      await page.waitForTimeout(700);

      const stuckElements = await page.evaluate(() => {
        const stuck = [];
        const cards = document.querySelectorAll('.spotlight-card, .service-card, .product-card, .new-offer-card, .section-title');
        cards.forEach(el => {
          const cs = window.getComputedStyle(el);
          if (cs.opacity === '0' || cs.visibility === 'hidden') {
            stuck.push({
              tag: el.tagName,
              class: el.className,
              text: el.innerText.slice(0, 30)
            });
          }
        });
        return stuck;
      });
      if (stuckElements.length > 0) {
        stuckElements.forEach(item => reportBug('MEDIUM', 'Stuck Invisible Element', pagePath, `<${item.tag} class="${item.class}"> "${item.text}" has opacity: 0`));
      }

      // 4. Check Internal Links and Anchor Targets
      const linkIssues = await page.evaluate(() => {
        const links = Array.from(document.querySelectorAll('a[href]'));
        const issues = [];
        for (const a of links) {
          const href = a.getAttribute('href');
          if (!href) continue;
          if (href.startsWith('#') && href.length > 1) {
            const targetId = href.substring(1);
            if (!document.getElementById(targetId) && !document.querySelector(`[name="${targetId}"]`)) {
              issues.push({ href, reason: `Target anchor #${targetId} not found in DOM` });
            }
          }
        }
        return issues;
      });
      if (linkIssues.length > 0) {
        linkIssues.forEach(issue => reportBug('MEDIUM', 'Broken Anchor Link', pagePath, `${issue.href} -> ${issue.reason}`));
      }

      // 5. Privacy Leaks Check (Forbidden strings)
      const privacyCheck = await page.evaluate(() => {
        const bodyText = document.body.innerText;
        const leaks = [];
        if (/Subhash\s*Annam/i.test(bodyText)) leaks.push('Subhash Annam');
        if (/Jyothsna\s*Sri/i.test(bodyText)) leaks.push('Jyothsna Sri');
        if (/\+91\s*93473/i.test(bodyText)) leaks.push('Personal phone number');
        return leaks;
      });
      if (privacyCheck.length > 0) {
        privacyCheck.forEach(item => reportBug('CRITICAL', 'Privacy Leak', pagePath, `Found private founder/contact token in DOM text: ${item}`));
      }

      // 6. Multi-Viewport Overflow Audit
      await page.evaluate(() => window.scrollTo(0, 0));
      await page.waitForTimeout(200);

      for (const vp of VIEWPORTS) {
        await page.setViewportSize({ width: vp.width, height: vp.height });
        await page.waitForTimeout(300);

        const overflow = await page.evaluate(() => {
          const docEl = document.documentElement;
          const body = document.body;
          const scrollW = Math.max(docEl.scrollWidth, body.scrollWidth);
          const clientW = docEl.clientWidth;
          return { hasOverflow: scrollW > clientW + 2, scrollW, clientW };
        });

        if (overflow.hasOverflow) {
          // Identify which elements are causing the overflow
          const overflowingElements = await page.evaluate(() => {
            const clientW = document.documentElement.clientWidth;
            const culprits = [];
            document.querySelectorAll('*').forEach(el => {
              const r = el.getBoundingClientRect();
              if (r.right > clientW + 3 && !el.classList.contains('cyber-grid') && !el.classList.contains('aurora-orb')) {
                culprits.push({
                  tag: el.tagName,
                  class: el.className,
                  id: el.id,
                  right: Math.round(r.right),
                  clientW
                });
              }
            });
            return culprits.slice(0, 4);
          });

          reportBug('HIGH', 'Horizontal Scroll Overflow', pagePath, `${vp.name} scrollWidth (${overflow.scrollW}px) > clientWidth (${overflow.clientW}px). Culprits: ${JSON.stringify(overflowingElements)}`);
        }
      }

      // 7. Page-Specific Functional Tests
      if (pagePath === '/') {
        // Check 3D hero canvas
        const heroCheck = await page.evaluate(() => {
          const vp = document.querySelector('.hero-3d-viewport');
          if (!vp) return 'missing viewport';
          const canvas = vp.querySelector('canvas');
          return {
            hasCanvas: !!canvas,
            hasWebGLClass: vp.classList.contains('has-webgl'),
            canvasWidth: canvas ? canvas.width : 0,
            canvasHeight: canvas ? canvas.height : 0
          };
        });
        if (!heroCheck.hasCanvas && !heroCheck.hasWebGLClass) {
          reportBug('HIGH', '3D Hero Engine', '/', 'Hero viewport missing WebGL canvas and fallback mark');
        }
      }

      if (pagePath === '/estimate/') {
        // Test estimator wizard steps
        const estimatorTest = await page.evaluate(async () => {
          const step1 = document.getElementById('step1');
          const step2 = document.getElementById('step2');
          const step3 = document.getElementById('step3');
          const step4 = document.getElementById('step4');
          const nextBtn = document.getElementById('btnNext1');
          const opt = document.querySelector('.opt-card');
          if (!step1 || !opt || !nextBtn) return 'Estimator elements missing';

          opt.click();
          nextBtn.click();
          const inStep2 = step2 && step2.classList.contains('active');

          const nextBtn2 = document.getElementById('btnNext2');
          if (nextBtn2) nextBtn2.click();
          const inStep3 = step3 && step3.classList.contains('active');

          const timelineOpt = document.querySelector('#step3 .opt-card');
          if (timelineOpt) timelineOpt.click();
          const calcBtn = document.getElementById('btnNext3');
          if (calcBtn) calcBtn.click();
          const inResult = step4 && step4.classList.contains('active');

          return { inStep2, inStep3, inResult };
        });
        if (!estimatorTest.inResult) {
          reportBug('HIGH', 'Estimator Flow', '/estimate/', `Estimator wizard failed to reach result screen: ${JSON.stringify(estimatorTest)}`);
        }
      }

      if (pagePath === '/contact/') {
        // Test contact form presence & inputs
        const formCheck = await page.evaluate(() => {
          const form = document.querySelector('form') || document.querySelector('.contact-form');
          if (!form) return 'No form found';
          const inputs = form.querySelectorAll('input, textarea, select, button[type="submit"]');
          return { inputCount: inputs.length };
        });
        if (typeof formCheck === 'string') {
          reportBug('HIGH', 'Contact Form', '/contact/', formCheck);
        }
      }

      await context.close();
    }

    console.log(`\n============================================================`);
    console.log(`BUG HUNT COMPLETE — TOTAL FINDINGS: ${findings.length}`);
    console.log(`============================================================\n`);

    const summary = {
      total: findings.length,
      critical: findings.filter(f => f.severity === 'CRITICAL'),
      high: findings.filter(f => f.severity === 'HIGH'),
      medium: findings.filter(f => f.severity === 'MEDIUM'),
      findings
    };

    fs.writeFileSync(
      'C:/Users/nagas/.gemini/antigravity/brain/73d357b8-8363-4a56-95a5-af17bf9f3712/bug_hunt_report.json',
      JSON.stringify(summary, null, 2)
    );

    console.log(JSON.stringify(summary, null, 2));

  } finally {
    await browser.close();
    server.close();
  }
}

runBugHunt().catch(err => {
  console.error('Fatal Bug Hunt Error:', err);
  process.exit(1);
});
