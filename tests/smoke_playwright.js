const { chromium } = require('@playwright/test');

(async () => {
  try {
    const browser = await chromium.launch({
      channel: 'chrome',
      headless: true
    });
    const page = await browser.newPage();
    await page.setContent('<h1>VALIXIS Playwright Test</h1>');
    const title = await page.textContent('h1');
    console.log('Playwright successfully launched system Chrome! Content:', title);
    await browser.close();
  } catch (err) {
    console.error('Playwright launch error:', err);
    process.exit(1);
  }
})();
