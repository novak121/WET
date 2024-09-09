const nadpis = document.querySelector("#nadpis"),
    text = document.querySelector("#text"),
    tlacitko = document.querySelector("#tlacitko"),
    input = document.querySelector("#input");

const seznamSlov = ["hokus", "pokus", "stuff"];
let hadaneSlovo = seznamSlov[Math.floor(Math.random() * seznamSlov.length)];

// ze seznamu slov vybíráme náhodné slovo (přes jeho index)
console.log(hadaneSlovo);

// vytvoříme array odpovědí
let odpoved = [];

for (let i = 0; i < hadaneSlovo.length; i++) {
    odpoved[i] = "_";
}
// za každé písmeno z odpovědi (momentálné samá podtržítka) vypíše do HTML
for (let i = 0; i < odpoved.length; i++) {
    text.innerText += odpoved[i];
}

// tlačítku přidáme interakci
tlacitko.addEventListener("click", hadani);

function hadani() {
    // přijmeme input z HTML a přiřadíme ho proměnné písmeno
    let pismeno = input.value;
    input.value = "";
    // porovnáváme každé písmeno z hádaného slova s písmenem, které uživatel tipoval
    // pokud se rovnají, dosadíme písmeno do odpovědi
    for (let i = 0; i < hadaneSlovo.length; i++) {
        if (pismeno === hadaneSlovo[i]) {
            odpoved[i] = pismeno;
        }
    }
    text.innerText = "";
    // kaže písmeno z odpovědi vypíše do HTMl
    for (let i = 0; i < odpoved.length; i++) {
        text.innerText += odpoved[i];
    }
}
