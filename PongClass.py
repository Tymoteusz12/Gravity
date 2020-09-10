from functions import *

class Pong_ball:
    def __init__(self, x, y, radius):
        self.speed = 0
        self.pongMass = 1
        self.pongPos = Vector2(x, y)
        self.radius = radius
        self.velocity = Vector2()
        self.acceleration = Vector2()

    def drawPong(self):
        pygame.draw.circle(WindowObj.window, colors.pongOutlineColor, (int(self.pongPos.x), int(self.pongPos.y)), self.radius)
        pygame.draw.circle(WindowObj.window, colors.pongColor, (int(self.pongPos.x), int(self.pongPos.y)), self.radius-2)

    def pongMovement(self):
        self.velocity += self.acceleration
        self.pongPos.x += self.velocity.x
        self.pongPos.y += self.velocity.y
