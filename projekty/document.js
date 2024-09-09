let tlacitko = document.querySelector("#tlacitko")
let nadpis = document.getElementById("nadpis")





tlacitko.addEventListener("click", zmenNadpis)


function zmenNadpis() {
    nadpis.style.color = "red"
    nadpis.innerText = input.value
}