#SHIT IS DONE BOYS AND GIRLS


import pygame
FPS = 80
SIZE = [1050, 1050]




#colors
bg = [182, 194, 217]
blue = [115,220,222]
orange = [251,170,60]
grey = [74,102,112]
white = [255,255,255]

 
# Field Width
FW = 50

LEFTBORDER = 20
TOPBORDER = 20
TILESIZE = 20

class player():

    def __init__(self,color, startingPos):
      self.trail = []
      self.location = startingPos
      self.color = color
      self.direction = ""#previous direction
        

    def move(self,direction,opponentsTrail,opponentsLocation):
      oldLocation = []
      oldLocation.append(self.location[0])
      oldLocation.append(self.location[1])

      if direction == "R":
        if self.location[0] >= FW - 1:
            return False

        if self.direction == "L":
          self.location = self.location[0] - 1
          self.direction = "L"

        else:
          self.location[0] = self.location[0] + 1
          self.direction = direction
              
        self.trail.append(oldLocation)



      elif direction == "L":
        if self.location[0] <= 0:

          return False
        
        if self.direction == "R":
          self.location[0] = self.location[0] + 1
          self.direction = "R"


        else:
          self.location[0] = self.location[0] - 1
          self.direction = direction

        
        self.trail.append(oldLocation)



      elif direction == "U":
        if self.location[1] <= 0:
          return False
        if self.direction == "D":
          self.location[1] = self.location[1] + 1
          self.direction = "D"


        else:
          self.location[1] = self.location[1] - 1
          self.direction = direction

        self.trail.append(oldLocation)




      elif direction == "D":
        if self.location[1] >= FW - 1:
          return False
        if self.direction == "U":
          self.location[1] = self.location[1] -1
          self.direction = "U"

        else:
          self.location[1] = self.location[1] + 1
          self.direction = direction
        self.trail.append(oldLocation)
      


      for point in self.trail:# collision detector
        if self.location[0] == point[0]:
          if self.location[1] == point[1]:
            return False

      for point in opponentsTrail:# collision detector
        if self.location[0] == point[0]:
          if self.location[1] == point[1]:
            return False





    def getLocation(self):
      return self.location 
      
    def getColor(self):
      return self.color 

    def getTrail(self):
      return self.trail



class window():
    def __init__(self):
      self.direction1 = ""
      self.direction2 = ""
      self.playing = True
      self.player = -1
      self.player1 = player(blue, [5,1])
      self.player2 = player(orange, [44,1])
      self.field = []
      self.clock = pygame.time.Clock()
      self.winner = ""
      

      #makes list for of rectangels for draw field funciton
      for i in range (FW):
        row = []
        for j in range(FW):
          fieldRect = pygame.Rect(LEFTBORDER + (j * TILESIZE), TOPBORDER + (i * TILESIZE), TILESIZE, TILESIZE)
          row.append(fieldRect)
        
        self.field.append(row)
    

    def drawField(self):
        for row in self.field:
          for rect in row:
            pygame.draw.rect(self.screen,grey,rect)

    def drawField1(self):
        for row in self.field:
          for rect in row:
            pygame.draw.rect(self.screen,white,rect,width = 1)
  
  

    def drawPlayer1(self):
      rect = pygame.Rect(LEFTBORDER + (self.player1.location[0] * TILESIZE), TOPBORDER + (self.player1.location[1] * TILESIZE), TILESIZE, TILESIZE)

      pygame.draw.rect(self.screen , blue ,rect)

    def drawPlayer2(self):
      rect = pygame.Rect(LEFTBORDER + (self.player2.location[0] * TILESIZE), TOPBORDER + (self.player2.location[1] * TILESIZE), TILESIZE, TILESIZE)

      pygame.draw.rect(self.screen , orange,rect)

    def drawPlayer1Trail(self):
        for point in self.player1.getTrail():
          rect = pygame.Rect(LEFTBORDER + (point[0] * TILESIZE), TOPBORDER + (point[1] * TILESIZE), TILESIZE, TILESIZE)

          pygame.draw.rect(self.screen , blue ,rect)
          
    def drawPlayer2Trail(self):
            for point in self.player2.getTrail():
              rect = pygame.Rect(LEFTBORDER + (point[0] * TILESIZE), TOPBORDER + (point[1] * TILESIZE), TILESIZE, TILESIZE)

              pygame.draw.rect(self.screen , orange ,rect)     

    def main(self):
        self.screen = pygame.display.set_mode(SIZE)


        while self.playing == True:
            for event in pygame.event.get():
              pressed_keys = pygame.key.get_pressed()

              if event.type == pygame.QUIT:
                return False
      
      #player one controls
    
              if pressed_keys[pygame.K_UP]:
                self.direction1 = "U"

              
              if pressed_keys[pygame.K_DOWN]:
                self.direction1 = "D"



              if pressed_keys[pygame.K_LEFT]:
                self.direction1 = "L"
              
              if pressed_keys[pygame.K_RIGHT]:
                self.direction1 = "R"

    #player two controls


              if pressed_keys[pygame.K_w]:
                self.direction2 = "U"
              
              if pressed_keys[pygame.K_s]:
                self.direction2 = "D"

              if pressed_keys[pygame.K_a]:
                self.direction2 = "L"


              
              if pressed_keys[pygame.K_d]:
                self.direction2 = "R"
                self.player = 2

          #updates the window screen
            self.screen.fill(bg)
            self.drawField()
            self.drawField1()

            self.drawPlayer1()
            self.drawPlayer2()

            self.drawPlayer1Trail()
            self.drawPlayer2Trail()

            playing1 = self.player1.move(self.direction1,self.player2.getTrail(),self.player2.getLocation())
            playing2 = self.player2.move(self.direction2,self.player1.getTrail(),self.player1.getLocation())

            if playing1 == False:
              self.winner = "player 2"
              self.playing = False
            elif playing2 == False:
              self.winner = "player 1"
              self.playing = False
          

            if self.player1.getLocation()[0] == self.player2.getLocation()[0]:
              if self.player1.getLocation()[1] == self.player2.getLocation()[1]:
                print("The game is a tie")
                self.playing = False

            elif self.playing == False:
                print("The Winner is" , self.winner)


            pygame.display.update()
            self.clock.tick(FPS)







if __name__ == "__main__":
  win = window()

  win.main()
