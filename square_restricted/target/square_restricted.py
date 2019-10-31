from pyp5js import *
from random import choice

POINTS = [(0, 0), (0, 800), (800, 800), (800, 0)]
p = POINTS[0]
last = p

def halfway(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def setup():
    createCanvas(800, 800)
    background(200)

def draw():
    global p
    global last
    for _ in range(20):
        sampled = choice(POINTS)
        if last != sampled:
            p = halfway(p, sampled)
            point(*p)
        last = sampled