function prevod(km) {
    let mile = km * 0.613;
    console.log(mile);
}

prevod(10);

console.log(prevod(50));
let vysledekPrevodu = prevod(30);

console.log(prevod(50));
let vysledekPrevodu = prevod(30);

let textvHTML = document.querySelector("#text");
textvHTML.innerText = prevod(50);
