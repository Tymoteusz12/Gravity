import sys, math, pygame
from typing import NamedTuple
from dataclasses import dataclass

pygame.init()
clock = pygame.time.Clock()

class Const(NamedTuple):
    pongRadius : int
    centralObjectSize : int
    resolution: tuple
    centralObjectPos: tuple

class Color(NamedTuple):
    accLineColor: tuple
    velLineColor: tuple
    pongOutlineColor: tuple
    pongColor: tuple
    centralObjectColor: tuple
    black: tuple

class WindowStruct(NamedTuple):
    resolution: tuple

class TimeStruct(NamedTuple):
    tickrate: int

class PhysicsStruct(NamedTuple):
    centralObjectMass: float
    constG: float

constant = Const(
    10, 100, (1024, 800), (512, 400)
)

colors = Color(
    (255, 0, 0), (255, 255, 255), (255, 100, 100),
    (0, 100, 0), (0, 128, 0), (0, 0, 0)
)

winStruct = WindowStruct(
    (1024, 800)
)

timeStruct = TimeStruct(
    60
)

physicsStruct = PhysicsStruct(
    5.972 * 10 ** 19, 6.674 * 10 ** (-17)
)

@dataclass
class StatesClass:
    pongInstance : object
    delta: float = 0
    click: bool = False
    space: bool = False

@dataclass
class WindowClass:
    window : object = pygame.display.set_mode(winStruct.resolution)

@dataclass
class PhysicsRelatedClass:
    speedMagnitude : float = 0

States = StatesClass(0)
WindowObj = WindowClass()
PhysicsRelated = PhysicsRelatedClass()






