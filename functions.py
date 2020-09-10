from config import *
from pygame.math import Vector2
def calcInitiationalSpeedVec(speedVec):
    States.pongInstance.velocity = PhysicsRelated.speedMagnitude * speedVec.normalize() / 2

def calcDistanceVec():
    distance = Vector2(512 - States.pongInstance.pongPos.x, 400 - States.pongInstance.pongPos.y)
    return distance

def findAccVec(distanceVec):
    Force = physicsStruct.constG * physicsStruct.centralObjectMass / distanceVec.length() ** 2
    States.pongInstance.acceleration = Force * distanceVec.normalize() / States.pongInstance.pongMass

def drawPongAccMagnitude():
    if States.click and States.space:
        pygame.draw.line(WindowObj.window, colors.accLineColor, (int(States.pongInstance.pongPos.x), int(States.pongInstance.pongPos.y)), ((States.pongInstance.acceleration.x*1000+States.pongInstance.pongPos.x),(States.pongInstance.acceleration.y*1000+States.pongInstance.pongPos.y)), 2)

def drawPongSpeed(): #rysuje predkosc
    if States.click and States.space:
        pygame.draw.line(WindowObj.window, colors.velLineColor, (int(States.pongInstance.pongPos.x), int(States.pongInstance.pongPos.y)), (States.pongInstance.velocity.x * 16 + States.pongInstance.pongPos.x, States.pongInstance.velocity.y * 16 + States.pongInstance.pongPos.y), 2)

def redraw():
    WindowObj.window.fill(colors.black)
    States.pongInstance.drawPong()
    drawPongAccMagnitude()
    drawPongSpeed()

def drawSpeedMagnitude(cursorPos):
    pygame.draw.line(WindowObj.window, colors.velLineColor, [States.pongInstance.pongPos.x, States.pongInstance.pongPos.y], cursorPos, 3)

def drawCentralObject():
    pygame.draw.circle(WindowObj.window, colors.centralObjectColor, constant.centralObjectPos, constant.centralObjectSize)

def calcGravityForce(): #liczenie siły grawitacji
    if States.click and States.space:
        distanceVec = calcDistanceVec()
        distanceVecLength = distanceVec.length()

        if distanceVecLength != 0:
            findAccVec(distanceVec)
            States.pongInstance.pongMovement()

def manageStatesAfterInstanceCreation():
    States.click = True
    States.space = False

def calcSpeedMagnitude(cursorPositionAfterClick, pongInstance):
    PhysicsRelated.speedMagnitude = math.sqrt((cursorPositionAfterClick[0] - pongInstance.pongPos.x) ** 2 + (cursorPositionAfterClick[1] - pongInstance.pongPos.y) ** 2) / 16  # liczę moc obliczając długosc wektora
    speedVec = Vector2((cursorPositionAfterClick[0] - pongInstance.pongPos.x), (cursorPositionAfterClick[1] - pongInstance.pongPos.y))  # wektor prędkosci
    States.space = True
    calcInitiationalSpeedVec(speedVec)

