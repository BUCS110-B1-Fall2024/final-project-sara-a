
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Ping Pong Game
## CS110 B1 Final Project fall, 2024

## Team Members

Sara Antin

***

## Project Description

It is going to simulate a ping pong game. both paddles are moveable by the player, for paddle 2, the player presses the up and down arrows to move up and down. and for paddle 1 the player presses the w and s keys to move up and down. the goal is to bounce the ball from pne paddle to the other. if player misses the game ends.

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. start menu
2. moveable paddle
3. gameover screen
4. obstacle paddle
5. bouncing ball

### Classes

- ball class: it makes the ball that moves between the two paddles for the game. this is what is getting bounced. if the paddles miss the ball then the game ends
- paddle class: this creates the two paddles. the player controls both paddles and they play the game against themself by moving each paddle up and down to bounce the ball off of.
- controller class: this is where i imported the ball and paddle to in order to use them and make the game

## ATP
test case 1: paddle movement
description: to make sure each paddle is moveable up and down by the specified keys.
steps:
start game
press up key
make sure right paddle moves up
press down key
make sure right paddle moves down
press w key
make sure left paddle moves up
press s key
make sure left paddle moves down
expected outcome: the left and right paddles will move up and down when the keys are pressed

test case 2: detect collisions
description: make sure the collisions between the ball and each paddle are detected correctly
test steps:
start the game
move right paddle to hit ball
ball should bounce off of paddle
move left paddle up to the top of the screen and let ball miss and go out of the screen
verify game ends after missed hit
expected outcome: ball should bounce off hit paddle and game should end after second paddle misses

test case 3: game over condition
description: make sure game ends when ball falls out of the screen
steps: 
start game
play until ball falls out of screen
make sure the game over screen that says which side won and how to either start again or end game appears
expected outcome: game should say "right/left player wins" "s to start again or e to end game"

test case 4: start menu
description: make sure game starts when enter key is pressed at the start menu
steps:
open game
make sure message that says to press enter to begin is displayed
press enter
ensure game begins
expected outcome: game will start once return key is pressed

test case 5: wrong keys pressed
steps:
start game
press wrong key at enter screen and/or while trying to move paddles
make sure program does not begin or move paddles
expected outcome: program responds by not doing anything when incorrect keys are pressed