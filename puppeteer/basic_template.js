const puppeteer = require("puppeteer");
const cheerio = require("cheerio");

async function main() {
    // Ir a la página
	const browser = await puppeteer.launch({ headless: false });
	const page = await browser.newPage ();
	await page.goto ("https://www.google.com/search?q=software");

    // Cargar HTML de la página
    const html = await page.content();
    const $ = cheerio.load(html);

    // Mostrar titulos por consola
    $("h3.LC20lb MBeuO DKV0Md").each(indexe, element) => console.log( $(element).text() )
}

main ();
