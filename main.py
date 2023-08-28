import pygame
import random

pygame.init()

gadget_pair = 1
ch = int(input("Enter your choice for the gadget pair(1 or 2): "))
if ch == 1:
    gadget_pair = 1
elif ch == 2:
    gadget_pair = 2

WIDTH, HEIGHT = 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

run = True

directions = [0, 1]  # 0 - TOP, 1 - BOTTOM
angles = [0, 1, 2]  # 0 - VEL(Y) = 2 * VEL(X), 1 - VEL(X) = VEL(Y), 2 - VEL(X) = 2 * VEL(Y)

# COLORS
WHITE = (255, 255, 255)
GREEN = (0, 180, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# BALL
radius = 15
ballX, ballY = WIDTH / 2 - radius, HEIGHT / 2 - radius
ballVelX, ballVelY = 0.3, 0.3
dummyBallX, dummyBallY = WIDTH / 2 - radius, HEIGHT / 2 - radius
dummyBallVelX, dummyBallVelY = 0.3, 0.3

# PADDLE
paddleWidth, paddleHeight = 20, 120
leftPaddleY = rightPaddleY = HEIGHT / 2 - paddleHeight / 2
leftPaddleX, rightPaddleX = 100 - paddleWidth / 2, WIDTH - (100 - paddleWidth / 2)
rightPaddleVel = leftPaddleVel = 0

secondLeftPaddleY = secondRightPaddleY = HEIGHT / 2 - paddleHeight / 2
secondLeftPaddleX, secondRightPaddleX = 100 - paddleWidth / 2, WIDTH - (100 - paddleWidth / 2)
secondRightPaddleVel = secondLeftPaddleVel = 0


def randomDirectionAngle():
    randomDirection = random.choice(directions)
    randomAngle = random.choice(angles)
    velocityX, velocityY = None, None
    if randomDirection == 0:
        if randomAngle == 0:
            velocityX, velocityY = 0.4, -0.8
        if randomAngle == 1:
            velocityX, velocityY = 0.4, -0.4
        if randomAngle == 2:
            velocityX, velocityY = 0.8, -0.4
    if randomDirection == 1:
        if randomAngle == 0:
            velocityX, velocityY = 0.4, 0.8
        if randomAngle == 1:
            velocityX, velocityY = 0.4, 0.4
        if randomAngle == 2:
            velocityX, velocityY = 0.8, 0.4

    return velocityX, velocityY


# GADGETS
leftGadget = rightGadget = 0
leftGadgetRemaining = rightGadgetRemaining = 5

player1 = player2 = 0

while run:

    wn.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rightPaddleVel = -0.6
            if event.key == pygame.K_DOWN:
                rightPaddleVel = 0.6
            if event.key == pygame.K_RIGHT and rightGadgetRemaining > 0:
                rightGadget = 1
            if event.key == pygame.K_LEFT and rightGadgetRemaining > 0:
                rightGadget = 2
            if event.key == pygame.K_w:
                leftPaddleVel = -0.6
            if event.key == pygame.K_s:
                leftPaddleVel = 0.6
            if event.key == pygame.K_d and leftGadgetRemaining > 0:
                leftGadget = 1
            if event.key == pygame.K_a and leftGadgetRemaining > 0:
                leftGadget = 2

            secondRightPaddleVel = rightPaddleVel
            secondLeftPaddleVel = leftPaddleVel

        if event.type == pygame.KEYUP:
            rightPaddleVel = 0
            leftPaddleVel = 0
            secondLeftPaddleVel = 0
            secondRightPaddleVel = 0

    # PADDLE MOVEMENT

    if leftPaddleY >= HEIGHT - paddleHeight:
        leftPaddleY = HEIGHT - paddleHeight

    if leftPaddleY <= 0:
        leftPaddleY = 0

    if rightPaddleY >= HEIGHT - paddleHeight:
        rightPaddleY = HEIGHT - paddleHeight

    if rightPaddleY <= 0:
        rightPaddleY = 0

    # SECOND PADDLE MOVEMENT
    if secondLeftPaddleY >= HEIGHT - paddleHeight:
        secondLeftPaddleY = HEIGHT - paddleHeight

    if secondLeftPaddleY <= 0:
        secondLeftPaddleY = 0

    if secondRightPaddleY >= HEIGHT - paddleHeight:
        secondRightPaddleY = HEIGHT - paddleHeight

    if secondRightPaddleY <= 0:
        secondRightPaddleY = 0

    # COLLISIONS WITH PADDLES
    # LEFT PADDLE

    if secondLeftPaddleY == leftPaddleY:
        if leftPaddleX <= ballX <= leftPaddleX + paddleWidth:
            if leftPaddleY <= ballY <= leftPaddleY + paddleHeight:
                ballX = leftPaddleX + paddleWidth
                dummyBallX = leftPaddleX + paddleWidth
                ballVelX *= -1
                dummyBallVelX *= -1
    else:
        if leftPaddleX <= ballX <= leftPaddleX + paddleWidth:
            if leftPaddleY <= ballY <= leftPaddleY + paddleHeight:
                ballX = leftPaddleX + paddleWidth
                dummyBallX = leftPaddleX + paddleWidth
                ballVelX *= -1
                dummyBallVelX *= -1
            if secondLeftPaddleX <= ballX <= secondLeftPaddleX + paddleWidth:
                if secondLeftPaddleY <= ballY <= secondLeftPaddleY + paddleHeight:
                    ballX = leftPaddleX + paddleWidth
                    dummyBallX = leftPaddleX + paddleWidth
                    ballVelX *= -1
                    dummyBallVelX *= -1

    # RIGHT PADDLE
    if secondRightPaddleY == rightPaddleY:
        if rightPaddleX <= ballX <= rightPaddleX + paddleWidth:
            if rightPaddleY <= ballY <= rightPaddleY + paddleHeight:
                ballX = rightPaddleX
                dummyBallX = rightPaddleX
                ballVelX *= -1
                dummyBallVelX *= -1
    else:
        if rightPaddleX <= ballX <= rightPaddleX + paddleWidth:
            if rightPaddleY <= ballY <= rightPaddleY + paddleHeight:
                ballX = rightPaddleX
                dummyBallX = rightPaddleX
                ballVelX *= -1
                dummyBallVelX *= -1
        if secondRightPaddleX <= ballX <= secondRightPaddleX + paddleWidth:
            if secondRightPaddleY <= ballY <= secondRightPaddleY + paddleHeight:
                ballX = rightPaddleX
                dummyBallX = rightPaddleX
                ballVelX *= -1
                dummyBallVelX *= -1

    # GADGET ACTION
    if gadget_pair == 1:
        if leftGadget == 1:
            if leftPaddleX <= ballX <= leftPaddleX + paddleWidth:
                if leftPaddleY <= ballY <= leftPaddleY + paddleHeight:
                    ballX = leftPaddleX + paddleWidth
                    ballVelX *= -2
                    dummyBallVelX *= -2
                    leftGadget = 0
                    leftGadgetRemaining -= 1
        elif leftGadget == 2:
            leftPaddleY = ballY
            leftGadget = 0
            leftGadgetRemaining -= 1

        if rightGadget == 1:
            if rightPaddleX <= ballX <= rightPaddleX + paddleWidth:
                if rightPaddleY <= ballY <= rightPaddleY + paddleHeight:
                    ballX = rightPaddleX
                    ballVelX *= -2
                    dummyBallVelX *= -2
                    rightGadget = 0
                    rightGadgetRemaining -= 1
        elif rightGadget == 2:
            rightPaddleY = ballY
            rightGadget = 0
            rightGadgetRemaining -= 1
    elif gadget_pair == 2:
        if leftGadget == 1:
            if leftPaddleX <= ballX <= leftPaddleX + paddleWidth:
                if leftPaddleY <= ballY <= leftPaddleY + paddleHeight:
                    ballX = leftPaddleX + paddleWidth
                    dummyBallX = leftPaddleX + paddleWidth
                    ballVelX *= -1
                    dummyBallVelX *= -1
                    dummyBallVelY *= -1
                    leftGadget = 0
                    leftGadgetRemaining -= 1
        elif leftGadget == 2:
            secondLeftPaddleY = leftPaddleY + 200
            leftGadget = 0
            leftGadgetRemaining -= 1
        if rightGadget == 1:
            if rightPaddleX <= ballX <= rightPaddleX + paddleWidth:
                if rightPaddleY <= ballY <= rightPaddleY + paddleHeight:
                    ballX = rightPaddleX
                    dummyBallX = rightPaddleX
                    ballVelX *= -1
                    dummyBallVelX *= -1
                    dummyBallVelY *= -1
                    rightGadget = 0
                    rightGadgetRemaining -= 1
        elif rightGadget == 2:
            secondRightPaddleY = rightPaddleY + 200
            rightGadget = 0
            rightGadgetRemaining -= 1


    # BALL MOVEMENT
    if ballY <= 0 + radius or ballY >= HEIGHT - radius:
        ballVelY *= -1
    if dummyBallY <= 0 + radius or dummyBallY >= HEIGHT - radius:
        dummyBallVelY *= -1

    if ballX >= WIDTH - radius:
        player1 += 1
        ballX, ballY = WIDTH / 2 - radius, HEIGHT / 2 - radius
        dummyBallX, dummyBallY = WIDTH / 2 - radius, HEIGHT / 2 - radius
        secondLeftPaddleY = leftPaddleY
        secondRightPaddleY = rightPaddleY
        ballVelX, ballVelY = randomDirectionAngle()
        dummyBallVelX, dummyBallVelY = ballVelX, ballVelY
        ballVelX *= -1
        dummyBallVelX *= -1

    if ballX <= 0 + radius:
        player2 += 1
        ballX, ballY = WIDTH / 2 - radius, HEIGHT / 2 - radius
        dummyBallX, dummyBallY = WIDTH / 2 - radius, HEIGHT / 2 - radius
        secondLeftPaddleY = leftPaddleY
        secondRightPaddleY = rightPaddleY
        ballVelX, ballVelY = randomDirectionAngle()
        dummyBallVelX, dummyBallVelY = ballVelX, ballVelY

    ballX += ballVelX
    ballY += ballVelY
    dummyBallX += dummyBallVelX
    dummyBallY += dummyBallVelY

    # PADDLES MOVEMENT VELOCITY
    rightPaddleY += rightPaddleVel
    leftPaddleY += leftPaddleVel
    secondRightPaddleY += secondRightPaddleVel
    secondLeftPaddleY += secondLeftPaddleVel

    # SCORE
    font = pygame.font.SysFont('calibri', 32)

    score = font.render("Player 1: " + str(player1), True, WHITE)
    wn.blit(score, (25, 25))

    score = font.render("Player 2: " + str(player2), True, WHITE)
    wn.blit(score, (825, 25))

    gadgetsLeft1 = font.render("Gadget left: " + str(leftGadgetRemaining), True, WHITE)
    wn.blit(gadgetsLeft1, (25, 65))

    gadgetsLeft2 = font.render("Gadget left: " + str(rightGadgetRemaining), True, WHITE)
    wn.blit(gadgetsLeft2, (825, 65))

    # OBJECTS
    # BALL
    pygame.draw.circle(wn, WHITE, (ballX, ballY), radius)
    # 2 ORIGINAL PADDLES
    pygame.draw.rect(wn, GREEN, pygame.Rect(leftPaddleX, leftPaddleY, paddleWidth, paddleHeight))
    pygame.draw.rect(wn, GREEN, pygame.Rect(rightPaddleX, rightPaddleY, paddleWidth, paddleHeight))
    # DUMMY BALL
    pygame.draw.circle(wn, WHITE, (dummyBallX, dummyBallY), radius)
    # 2 ADDITIONAL PADDLES
    pygame.draw.rect(wn, GREEN, pygame.Rect(secondLeftPaddleX, secondLeftPaddleY, paddleWidth, paddleHeight))
    pygame.draw.rect(wn, GREEN, pygame.Rect(secondRightPaddleX, secondRightPaddleY, paddleWidth, paddleHeight))

    if leftGadget == 1:
        pygame.draw.circle(wn, RED, (leftPaddleX + 10, leftPaddleY + 10), 4)
    if rightGadget == 1:
        pygame.draw.circle(wn, RED, (rightPaddleX + 10, rightPaddleY + 10), 4)

    # END SCREEN
    winningFont = pygame.font.SysFont('calibri', 100)
    if player1 >= 5:
        wn.fill(BLACK)
        endScreen = winningFont.render("PLAYER 1 WON!", True, WHITE)
        wn.blit(endScreen, (200, 250))

    if player2 >= 5:
        wn.fill(BLACK)
        endScreen = winningFont.render("PLAYER 2 WON!", True, WHITE)
        wn.blit(endScreen, (200, 250))

    pygame.display.update()

