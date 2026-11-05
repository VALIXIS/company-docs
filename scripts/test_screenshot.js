const { chromium } = require('playwright');
const path = require('path');
const http = require('http');
const fs = require('fs');

const PORT = 4199;
const ROOT_DIR = path.resolve(__dirname, '..');

const server = http.createServer((req, res) => {
  let reqPath = decodeURI(req.url.split('?')[0]);
  if (reqPath.endsWith('/')) reqPath += 'index.html';
  let filePath = path.join(ROOT_DIR, reqPath);
  if (!fs.existsSync(filePath)) {
    res.writeHead(404);
    res.end('404');
    return;
  }
  const ext = path.extname(filePath).toLowerCase();
  const mime = {
    '.html': 'text/html',
    '.css': 'text/css',
    '.js': 'application/javascript',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.svg': 'image/svg+xml'
  }[ext] || 'application/octet-stream';
  res.writeHead(200, { 'Content-Type': mime });
  fs.createReadStream(filePath).pipe(res);
});

(async () => {
  await new Promise(r => server.listen(PORT, r));
  console.log(`Server listening on http://localhost:${PORT}`);

  const browser = await chromium.launch({ channel: 'msedge', headless: true });
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });

  page.on('console', msg => console.log('PAGE LOG:', msg.type(), msg.text()));
  page.on('pageerror', err => console.log('PAGE ERROR:', err.message));

  await page.goto(`http://localhost:${PORT}/index.html`, { waitUntil: 'networkidle' });
  await page.waitForTimeout(2500);

  const screenshotPath = path.join(ROOT_DIR, 'scratch/local_server_hero.png');
  await page.screenshot({ path: screenshotPath, fullPage: false });
  console.log('Saved screenshot to:', screenshotPath);

  await browser.close();
  server.close();
})();
