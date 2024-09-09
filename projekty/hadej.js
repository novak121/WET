const nadpis = document.querySelector("#nadpis"),
    text = document.querySelector("#text")
    tlacitko = document.querySelector("#tlacitko")
    input = = document.querySelector("#input")

    let hadaneSlovo = "opice"

    let odpoved = []

    for (let i = 0; i < hadaneSlovo.length; i++) {
        odpoved[i] = "_"
    }

    for (let i = 0; i < odpoved.length; i++) {
        text.innerText += odpoved[i]
   }

   tlacitko.addEventListener("click",hadani) 

   
   function hadani() {
        let pismeno = input.value
        for (let i = 0; i < hadaneSlovo.length; i++) {
        if (pismeno === hadaneSlovo[i]) {

        }
   }
}
