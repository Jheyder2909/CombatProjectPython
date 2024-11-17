import Sprites

maps = Sprites.Frames("Map")

class Map:
    def __init__(self, numero) -> None:
        self.art = maps.getFrame(numero)
        self.lista = set()
    
    def print(self, stdscr):
            for y, LIST in enumerate(self.art):
                for x in LIST:
                    stdscr.addch(y, x, "&" )
                    self.lista.add((y, x))

    def getChar(self, y, x):

        if (y, x) in self.lista:
            return True 
        return False

    
        """
        try:
            test = self.art[y][x]
        except IndexError as e:
           return False
        return True
        #if self.lista.__contains__((y, x)):
        #     return True
        #return False
        """