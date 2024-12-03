class Ball:
   def __init__(self, x, y, radius, x_speed, y_speed, color):
       self.x = x
       self.y = y
       self.radius = radius
       self.x_speed = x_speed
       self.y_speed = y_speed
       self.color = color
       self.initialize_x = x
       self.initialize_y = y
      
   def move(self, screen_height):
       self.x += self.x_speed
       self.y += self.y_speed
       if self.y - self.radius <= 0 or self.y + self.radius >= screen_height:
           self.y_speed = -self.y_speed
      
   def reset_ball(self):
       self.x = self.initialize_x
       self.y = self.initialize_y
       self.x_speed *= -1
       self.y_speed *= -1