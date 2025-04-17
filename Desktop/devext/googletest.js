const { Builder } = require('selenium-webdriver');
(async function openGoogle() {
    let driver = await new Builder().forBrowser('chrome').build();
    try {
        await driver.get('https://www.google.com');
        await driver.sleep(3000);
    } finally {
        await driver.quit();
    }
})();
