const { chromium } = require('playwright');
const path = require('path');
const http = require('http');
const fs = require('fs');

const PORT = 4210;
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
  const browser = await chromium.launch({ channel: 'msedge', headless: true });
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });

  await page.goto(`http://localhost:${PORT}/index.html#leadership`, { waitUntil: 'networkidle' });
  await page.waitForTimeout(1000);

  const leadershipSection = await page.$('.leadership-grid');
  if (leadershipSection) {
    const screenshotPath = path.join(ROOT_DIR, 'scratch/monogram_avatars_screenshot.png');
    await leadershipSection.screenshot({ path: screenshotPath });
    console.log('Saved leadership section screenshot to:', screenshotPath);
  } else {
    console.log('leadership-grid not found');
  }

  await browser.close();
  server.close();
})();
