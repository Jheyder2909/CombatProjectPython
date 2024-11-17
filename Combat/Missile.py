# Missile.py
import math

class Missile:
    def __init__(self, player):
        radians = math.radians(player.angle * 15)
        self.x_pos = player.x_pos + math.cos(radians) * 15 - 1
        self.y_pos = player.y_pos + math.sin(radians) * 7 + 1
        self.angle = player.angle
        self.player = player
        self.bounce = 0
        #self.speed = 3  # Velocidad del misil
        self.x_vel = math.cos(math.radians(player.angle * 15)) #* self.speed
        self.y_vel = math.sin(math.radians(player.angle * 15)) #* self.speed

    def move(self):
       # radianes = math.radians(self.angle * 15)
       # self.x_pos += math.cos(radianes)
        #self.y_pos += math.sin(radianes)
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel

    def get_position(self):
        return (self.x_pos, self.y_pos)

    def print(self, stdscr):
        if not self.is_out_of_bounds():
            for y in range(3):
                for x in range (3):
                    stdscr.addch(int(self.y_pos) + y, int(self.x_pos) + x, '*')  # Representación del misil
        
    def is_out_of_bounds(self):
        return not (7 < self.x_pos < 463 and 22 <= self.y_pos < 116)

    
    def is_colliding_with_player(self, player):
        player_x, player_y = player.getPos()
        # Comprobamos si el misil está dentro del rango de colisión del jugador
        return (player_x - 10 <= self.x_pos <= player_x + 10) and (player_y - 10 <= self.y_pos <= player_y + 10)
    
    def collisionTank(self, tank) -> bool:
        dx: float = self.x_pos - tank.x_pos
        dy: float = self.y_pos - tank.y_pos
        # 100 es 10**2. 10 es el radio de los tanques
        if dx**2 + dy**2 <= 35:
            if tank.getChar() != self.player.getChar():
                return True
        return False

    # Si en la misma posicion q: mapa.Mue esta, hay un &, entonces true, sino false
    def collisionWall(self, map) -> bool:
        #return map.getChar(int(self.y_pos), int(self.x_pos))
        orientations = [(0, self.x_pos + 1, self.y_pos),      #right
                        (1, self.x_pos, self.y_pos - 1),      #up
                        (0, self.x_pos - 1, self.y_pos),      #left
                        (1, self.x_pos, self.y_pos + 1)]      #down
        if self.bounce < 3:
            for orientation in orientations:
                if map.getChar(int(orientation[2]), int(orientation[1])):
                    if orientation[0] == 0:
                        self.x_vel *= -1
                        self.bounce += 1
                    if orientation[0] == 1:
                        self.y_vel *= -1
                        self.bounce += 1
                    return True
            return False
        
    def canBounce(self): 
        if self.bounce < 2:
            return True
        return False
    
            #   return map.getChar(int(self.y_pos), int(self.x_pos)) return true or false if it touches a wall