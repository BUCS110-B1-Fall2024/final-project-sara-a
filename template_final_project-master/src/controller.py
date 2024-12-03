import pygame
from ball import Ball
from paddle import Paddle


class controller:
   def __init__(self):
       pygame.init()
       self.screen = pygame.display.set_mode(800, 800)
      
       self.paddle1 = Paddle(50, 300, 20, 100, (255, 255, 255), 10, 800)
       self.paddle2 = Paddle(730, 300, 20, 100, (255, 255, 255), 10, 800)
       self.ball = Ball(400, 400, 10, 5, 5, (255, 255, 255))
      
   def mainloop(self):
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
       self.detect_collisions()
      
       self.redraw()
      
       pygame.display.flip()
      
       self.gameoverloop
  
   def detect_collisions(self):
       args: None
       return None
   def redraw(self):
       args: None
       return None
   def gameoverloop(self):
       args: None
       return None
