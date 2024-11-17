import curses
import Sprites
import math
import time
import bisect

class Player:
    def __init__(self, player) -> None:
        if player:
            self.frames = Sprites.Frames("Player1")
            self.x_pos, self.y_pos = 20, 55.5
            self.angle = 0
            self.direccion = 1
            self.char = "#"
        else:
            self.frames = Sprites.Frames("Player2")
            self.x_pos, self.y_pos = 400, 55
            self.angle = 12
            self.direccion = -1
            self.char = "|"
        
        self.currentFrame = self.frames.getFrame(self.angle)
        self.missileTime = time.time()

    def getPos(self):
        return (self.x_pos, self.y_pos)
    
    def getChar(self):
        return self.char
    
    def updateFrame(self, key):
        if key == "d" or key == "j":
            self.angle = (self.angle + self.direccion) % 24
            self.currentFrame = self.frames.getFrame(self.angle)
        
        elif key == "a" or key == "l":
            self.angle = (self.angle - self.direccion) % 24
            self.currentFrame =  self.frames.getFrame(self.angle)

    def print(self, stdscr):
            for y, LIST in enumerate(self.currentFrame):
                for x in LIST:
                    stdscr.addch(int(self.y_pos) + y -5, int(self.x_pos) + x -15, self.char)

    def collisionWall(self, map, d, avancex, avancey) -> bool:

            orientations = [(0, avancex  + 5, avancey),      #right
                        (1, avancex, avancey +  5),      #up
                        (0, avancex - 8 , avancey),      #left
                        (1, avancex, avancey - 5)]      #down
            for orientation in orientations:
                if map.getChar(int(orientation[2]), int(orientation[1])):
                    return True
            return False

    
            #dx: float = self.x_pos - tank.x_pos
        #dy: float = self.y_pos - tank.y_pos
        # 100 es 10**2. 10 es el radio de los tanques
        # if dx**2 + dy**2 <= 35:
       # if d == "u":
       #     return map.getChar(int(avancey), int(avancex))             
        #if d == "d":
       #     return map.getChar(int(avancey), int(avancex))      

             

    def avanzar(self, key, sensibilidad, mapa):
        radianes = math.radians(self.angle * 15)

        avance_x = math.cos(radianes)
        avance_y = math.sin(radianes)



        if avance_y != 0:
            time.sleep(abs(avance_y/25) + sensibilidad)  

        if key == "w" or key == "i":
            if not self.collisionWall(mapa, "u", self.x_pos + avance_x, self.y_pos + avance_y):
                self.x_pos += avance_x
                self.y_pos += avance_y

        elif key == "s" or key == "k":
            if not self.collisionWall(mapa, 'd',  self.x_pos - avance_x, self.y_pos - avance_y):
                self.x_pos -= avance_x
                self.y_pos -= avance_y


        
