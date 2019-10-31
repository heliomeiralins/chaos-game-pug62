from pyp5js import *

from random import choice


POINTS = [(400, 100), (100, 600), (700, 600)]
p = POINTS[0]
last = p

    
def halfway(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def setup():
    createCanvas(800, 800)
    background(200)


def draw():
    global p
    for _ in range(5):
        p = halfway(p, choice(POINTS))
        point(*p)