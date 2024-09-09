let circles = []

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  
  for (let i = 0; i < 10; i++) {
    let createCircle = drawCircle()
  }
  
  for (let circle of circles) {
    let x = random(0, width)
    let y = random(0, height)
    ellipse(x, y, 25)
  }
  
}

function drawCircle() {
  let newCircle = {
    x: random(0, width), 
    y: random(0,height)
  }
}