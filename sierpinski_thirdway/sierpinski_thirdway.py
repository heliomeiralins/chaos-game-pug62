from pyp5js import *
from random import choice


POINTS = [(400, 100), (100, 600), (700, 600)]
p = POINTS[0]
last = p

    
def thirdway(p1, p2):
    return (2*p1[0] + p2[0]) / 3, (2*p1[1] + p2[1]) / 3


def setup():
    global p
    createCanvas(800, 800)
    background(200)
    for _ in range(1000000):
        p = thirdway(p, choice(POINTS))


def draw():
    global p
    for _ in range(500):
        p = thirdway(p, choice(POINTS))
        point(*p)