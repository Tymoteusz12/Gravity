from PongClass import *

while True:
    States.delta += clock.tick()/1000.0
    drawCentralObject()
    pygame.display.update()

    while States.delta > 1/timeStruct.tickrate:
        States.delta -= 1/timeStruct.tickrate
        calcGravityForce()

        if States.click:
            redraw()
            if not States.space:
                cursorPos = pygame.mouse.get_pos()
                drawSpeedMagnitude(cursorPos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                States.pongInstance = Pong_ball(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], constant.pongRadius)
                manageStatesAfterInstanceCreation()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not States.space:
                cursorPositionAfterClick = pygame.mouse.get_pos()
                calcSpeedMagnitude(cursorPositionAfterClick, States.pongInstance)

