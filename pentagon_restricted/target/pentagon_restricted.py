from pyp5js import *
from random import choice
 

POINTS = [(400, 50), (67, 292), (194, 683), (606, 683), (733, 292)]
p = POINTS[0]
last = p


def halfway(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def setup():
    createCanvas(800, 800)
    background(200)
    for p in POINTS:
        point(*p)


def draw():
    global p
    global last
    for _ in range(100):
        sampled = choice(POINTS)
        if last != sampled:
            p = halfway(p, sampled)
            point(*p)
        last = sampled