## Puppeteer
```bash
mkdir project
cd project
npm init --yes
npm add puppeteer cheerio

```

### Template básico
```js
const puppeteer = require("puppeteer");

async function main() {
	const browser = await puppeteer.launch({ headless: false });
	const page = await browser.newPage ();
	await page goto ("https://www.google.com");
}

main ();
```
