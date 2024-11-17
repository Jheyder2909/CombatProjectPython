import time
import keyboard
import Player

sensibilidad = 0.02
running = True

class Control:
    def __init__(self) -> None:
        pass

    def handle_keyboard(self, player1, player2):
        while running:
            # Mueve al jugador basado en la entrada
            if keyboard.is_pressed('w') and player1.x_pos > 7:
                player1.avanzar("w", sensibilidad)

            if keyboard.is_pressed('s') and player1.x_pos < 462:
                player1.avanzar("s", sensibilidad)

            if keyboard.is_pressed('a') :
                player1.updateFrame("a")

            if keyboard.is_pressed('d') :
                player1.updateFrame("d")


            if keyboard.is_pressed('i') and player2.x_pos > 7:
                player2.avanzar("i", sensibilidad)

            if keyboard.is_pressed('k') and player2.x_pos < 462:
                player2.avanzar("k", sensibilidad)

            if keyboard.is_pressed('j') :
                player2.updateFrame("j")

            if keyboard.is_pressed('l') :
                player2.updateFrame("l")


            if keyboard.is_pressed('q'):  # Salir con 'q'
                running = False
                
            time.sleep(0.03 + sensibilidad)
