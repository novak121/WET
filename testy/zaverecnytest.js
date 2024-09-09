const input = document.querySelector("predmety"),
out = document.querySelector("#out"),
tlacitko = document.querySelector("#tlacitko"),
nadpis = document.querySelector("#tlacitko"),
predmety = ["hrw", "mat", "aj", "čj", "fyz"]

tlacitko.addEventListener("click", pridejPredmet)

function pridejPredmet() {
    //kde je chybaaaaa
    predmety.push(input.value)
    out.innerText = ""
    for (let i = 0; i < predmety.length; i++) {
        out.innerText += predmety[i] + "\n"
    }
}