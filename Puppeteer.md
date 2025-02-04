## Puppeteer

### Inicializar proyecto
```bash
mkdir project
cd project
npm init --yes
npm add puppeteer cheerio

```

### Template básico
```js
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

    // Mostrar enlaces (seleccion de atributos)
    $("a").each(indexe, element) => console.log( $(element).attr("href") )
}

main ();
```



### Crear JSON
```js
// 1. usamos .map pq queremos que devuelva valores
// 2 .get() lo necesita cheerio para devolvefr resultado
const results = $("result-title")				
	•map((index, element) => {				
		const title = $(element).text();
		const url = $(element).attr("href");
		return { title, url };
	})
	•get();   
console. log (results);
```

### Seleccionar un nodo Hijo
```html
    <div class="result-container">
        <h2 class="result-title">Título 1</h2>
        <p>Descripción del primer resultado</p>
    </div>

    <div class="result-container">
        <h2 class="result-title">Título 2</h2>
        <p>Descripción del segundo resultado</p>
    </div>
```
```js
    $(".result-container").each(function() {
        	const titleElement = $(this).find(".result-title");
        	console.log(titleElement.text()); // Imprime "Título 1", "Título 2" en la consola
    });
```

### Visitar varias páginas 






