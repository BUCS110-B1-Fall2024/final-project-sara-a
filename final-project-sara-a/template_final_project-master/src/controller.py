import pygame
from src.ball import Ball
from src.paddle import Paddle

class Controller:
   def __init__(self):
      pygame.init()
      self.screen = pygame.display.set_mode((800, 800))
      self.clock = pygame.time.Clock()
    
      self.paddle1 = Paddle(50, 300, 20, 100, (255, 255, 255), 10, 800)
      self.paddle2 = Paddle(730, 300, 20, 100, (255, 255, 255), 10, 800)
      self.ball = Ball(400, 400, 10, 5, 5, (255, 255, 255))
   def start_menu(self):
       running = True
       while running:
           self.screen.fill("black")
           font = pygame.font.Font(None, 50)
           text = font.render("Ping Pong", True, (255, 255, 255))
           details_text = font.render("w to move left up, s to move left down", True, (255, 255, 255))
           more_text = font.render("up to move right up, down to move left down", True, (255, 255, 255))
           key_text = font.render("keys to press:", True, (255, 255, 255))
           instruct_text = font.render("Press enter to begin", True, (255, 255, 255))
           self.screen.blit(text, (300, 200))
           self.screen.blit(instruct_text, (240, 300))
           self.screen.blit(details_text, (50, 500))
           self.screen.blit(more_text, (50, 600))
           self.screen.blit(key_text, (240, 450))
           pygame.display.flip()
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit()
                   exit()
               if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                   running = False
   def detect_collisions(self):
       if self.paddle1.x <= self.ball.x - self.ball.radius <= self.paddle1.x + self.paddle1.width:
           if self.paddle1.y <= self.ball.y <= self.paddle1.y +self.paddle1.height:
               self.ball.x_speed = -self.ball.x_speed
               
       if self.paddle2.x <= self.ball.x - self.ball.radius <= self.paddle2.x + self.paddle1.width:
           if self.paddle2.y <= self.ball.y <= self.paddle2.y + self.paddle2.height:
               self.ball.x_speed = -self.ball.x_speed
              
       if self.ball.y - self.ball.radius <= 0 or self.ball.y + self.ball.radius >= 800:
           self.ball.y_speed = -self.ball.y_speed
       if self.ball.x - self.ball.radius < 0:
           self.gameoverloop("Right Player")
       if self.ball.x + self.ball.radius > 800:
           self.gameoverloop("Left Player")
       
   def redraw(self):
       self.screen.fill("black")
       pygame.draw.rect(self.screen, self.paddle1.color, (self.paddle1.x, self.paddle1.y, self.paddle1.width, self.paddle1.height))
       pygame.draw.rect(self.screen, self.paddle2.color, (self.paddle2.x, self.paddle2.y, self.paddle2.width, self.paddle2.height))
       pygame.draw.circle(self.screen, self.ball.color, (self.ball.x, self.ball.y), self.ball.radius)
       pygame.draw.line(self.screen, (255, 255, 255), (400, 0), (400, 800), 1)
  
   def gameoverloop(self, winner):
       while True:
           self.screen.fill("black")
           font = pygame.font.Font(None, 74)
           win_text = font.render(f"{winner} wins", True, (255, 255, 255))
           instruct_text = font.render("S to start again or E to end game", True, (255, 255, 255))
           self.screen.blit(win_text, (200, 200))
           self.screen.blit(instruct_text, (5, 400))
           pygame.display.flip()
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit()
                   exit()
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_s:
                       self.reset_game()
                       return
                   if event.key == pygame.K_e:
                       pygame.quit()
                       exit()
   def reset_game(self):
       self.ball.reset_ball()
       self.paddle1.y = 300
       self.paddle2.y = 300
                      
   def mainloop(self):
      self.start_menu()
      running = True
      while running:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
                  pygame.quit()
                  exit()
       keys = pygame.key.get_pressed()
       if keys[pygame.K_UP]:
           self.paddle2.move_up()
       if keys[pygame.K_DOWN]:
           self.paddle2.move_down()
       if keys[pygame.K_w]:
           self.paddle1.move_up()
       if keys[pygame.K_s]:
           self.paddle1.move_down()
      
       self.ball.move(400)
       self.detect_collisions()
       self.redraw()
       pygame.display.flip()
       self.clock.tick(60)
    