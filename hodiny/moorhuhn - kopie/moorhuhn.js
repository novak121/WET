let panaci = []
let panakImage
let speed = 6
let score = 0

function preload() {
    panakImage = loadImage("panak.png")
}

function setup() {
    createCanvas(window.innerWidth, window.innerHeight)

    setInterval(function () {
        let newPanak = {
            x: random(0, window.innerWidth),
            y: random(0, window.innerHeight),
        }
        panaci.push(newPanak)
    }, 1000)
}

function draw() {
    background(255)

    panakImage.resize(200, 0)

    textSize(16)
    textAlign(RIGHT, TOP)
    text("Score" + score, width - 100, 10)

    for (let panak of panaci) {
        image(panakImage, panak.x, panak.y)
        panak.x -= speed
        if (panak.x < 0) {
            let index = panaci.indexOf(panak)
            panaci.splice(index, 1)
            score--
        }
    }
}

function mouseClicked() {
    panaci.forEach((panak, index) => {
        if (
            mouseX >= panak.x &&
            mouseX <= panak.x + panakImage.width &&
            mouseY >= panak.y &&
            mouseY <= panak.y + panakImage.height
        ) {
            panaci.splice(index, 1)
            console.log("111")
            score++
        }
    })
}
