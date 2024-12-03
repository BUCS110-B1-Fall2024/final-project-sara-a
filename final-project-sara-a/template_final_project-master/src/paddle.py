class Paddle:
   def __init__(self, x, y, width, height, color, speed, screen_height):
       self.x = x
       self.y = y
       self.width = width
       self.height = height
       self.color = color
       self.speed = speed
       self.screen_height = screen_height
      
   def move_up(self):
       if self.y - self.speed >= 0:
           self.y -= self.speed
          
   def move_down(self):
       if self.y + self.height + self.speed <= self.screen_height:
           self.y += self.speed
