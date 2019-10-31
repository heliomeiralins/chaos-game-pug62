from pyp5js import *

x = 0
y = 0

def setup():
    createCanvas(600, 600)
    background(255)

def drawPoint():
    stroke(34, 139, 34)
    strokeWeight(1)
    px = map(x, -2.1820, 2.6558, 0, width)
    py = map(y, 0, 9.9983, height, 0)
    point(px, py)

def nextPoint():
    global x
    global y
    r = random(1)
    if (r < 0.01):
        x, y =  0, 0.16 * y
    elif (r < 0.86):
        x, y =  0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
    elif (r < 0.93):
        x, y =  0.20 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
    else:
        x, y = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44


def draw():
  for i in range(100):
    drawPoint()
    nextPoint()