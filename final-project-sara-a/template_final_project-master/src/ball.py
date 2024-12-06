class Ball:
   def __init__(self, x, y, radius, x_speed, y_speed, color):
       self.x = x
       self.y = y
       self.radius = radius
       self.x_speed = x_speed
       self.y_speed = y_speed
       self.color = color
       self.initializex = x
       self.initializey = y
   def move(self, screen_height):
       self.x += self.x_speed
       self.y += self.y_speed
       if self.y - self.radius <= 0 or self.y + self.radius >= screen_height:
          self.y_speed = -self.y_speed
   def reset_ball(self):
       self.x = self.initializex
       self.y = self.initializey
       self.x_speed = abs(self.x_speed)
       self.y_speed *= -1