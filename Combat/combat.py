import curses
import time
import keyboard
import threading
import mapa
import Player
import Missile
import time
import Menu

sensibilidad = 0.0
player1 = Player.Player(True)
player2 = Player.Player(False)

t = time.thread_time

running = True
menu = True
tiempoRecarga = 2
# Tiempo de juego en segundos
game_duration = 1 * 60  # 5 minutos
start_time = time.time()  # Guardar el tiempo de inicio

map = mapa.Map(0)
misiles = []  # Lista para almacenar misiles

score_art = {
    '0': [
        " .d8888b.  ",
        "d88P  Y88b ",
        "888    888 ",
        "888    888 ",
        "888    888 ",
        "888    888 ",
        "Y88b  d88P ",
        "  Y8888P   "
    ],
    '1': [
        "    d888   ",
        "  d88888  ",
        "     888  ",
        "     888  ",
        "     888  ",
        "     888   ",
        "     888   ",
        "   8888888  "
    ],
    '2': [
        " .d8888b.  ",
        "d88P  Y88b ",
        "       888 ",
        "     .d88P ",
        " .od888P  ",
        "d88P      ",
        "888       ",
        "888888888  "
    ],
    '3': [
         " .d8888b.  ",
        "d88P  Y88b ",
        "     .d88P ",
        "    8888  ",
        "      Y8b. ",
        "888    888 ",
        "Y88b  d88P ",
        "  Y8888P  "
    ],
    '4': [
        "    d8888  ",
        "   d8P888  ",
        "  d8P 888  ",
        " d8P  888  ",
        "d88   888  ",
        "8888888888 ",
        "      888  ",
        "      888  "
    ],
    '5': [
        "  888888888  ",
        "  888        ",
        "  888        ",
        "  8888888b.  ",
        "       Y88b  ",
        "        888  ",
        " Y88b  d88P  ",
        "  Y8888P    "
    ],
    '6': [
        " .d8888b.  ",
        "d88P  Y88b ",
        "888        ",
        "888d888b.  ",
        "888P  Y88b ",
        "888    888 ",
        "Y88b  d88P ",
        "  Y8888P  "
    ],
    '7': [
        "8888888888 ",
        "      d88P ",
        "     d88P  ",
        "    d88P   ",
        " 88888888  ",
        "  d88P     ",
        " d88P      ",
        "d88P       "
    ],
    '8': [
        " .d8888b.  ",
        "d88P  Y88b ",
        "Y88b. d88P ",
        "  Y88888  ",
        ".d8P  Y8b. ",
        "888    888 ",
        "Y88b  d88P ",
        "  Y8888P  "
    ],
    '9': [
        " .d8888b.  ",
        "d88P  Y88b ",
        "888    888 ",
        "Y88b. d888 ",
        "  Y888P888 ",
        "       888 ",
        "Y88b  d88P ",
        "  Y8888P   "

    ],
    ':': [
        "           ",
        "    88     ",
        "    88     ",
        "           ",
        "    88     ",
        "    88     ",
        "           ",
        "           "
    ]
}

def print_timer_ascii(stdscr, elapsed_time):
    minutes, seconds = divmod(elapsed_time, 60)
    timer_str = f"{int(minutes):02}:{int(seconds):02}"  # Formato MM:SS

    # Convertir cada carácter del tiempo a su representación ASCII
    timer_lines = [""] * 8  # 8 líneas para el arte ASCII

    for char in timer_str:
        for i in range(8):
            timer_lines[i] += score_art[char][i] + "  "  # Agregar un espacio entre los dígitos

    # Imprimir las líneas del temporizador en la pantalla
    for i in range(8):
        stdscr.addstr(6 + i, 200, timer_lines[i])  # Imprimir en la posición deseada

def print_score(stdscr, score1, score2, offset=0):
    score1_str = str(score1)
    score2_str = str(score2)

    # Preparar las líneas para mostrar la puntuación
    score1_lines = [""] * 8  # Líneas para la puntuación del Jugador 1
    score2_lines = [""] * 8  # Líneas para la puntuación del Jugador 2

    # Construir las líneas de puntuación para el Jugador 1
    for digit in score1_str:
        for i in range(8):
            score1_lines[i] += score_art[digit][i]

    # Construir las líneas de puntuación para el Jugador 2
    for digit in score2_str:
        for i in range(8):
            score2_lines[i] += score_art[digit][i]

    # Imprimir las líneas de puntuación en la pantalla
    for i in range(8):
        stdscr.addstr(i + offset, 60, score1_lines[i])  # Imprimir la puntuación del Jugador 1 en la columna 0
        stdscr.addstr(i + offset, 390, score2_lines[i])  # Imprimir la puntuación del Jugador 2 en la columna 40
def handle_keyboard():
    global player1, player2, running, sensibilidad, map, misiles, menu, start_time
    while running:
        # Mueve al jugador basado en la entrada
        if keyboard.is_pressed('w'):
            player1.avanzar("w", sensibilidad, map)

        if keyboard.is_pressed('s'):
            player1.avanzar("s", sensibilidad, map)

        if keyboard.is_pressed('a') :
            player1.updateFrame("a")

        if keyboard.is_pressed('d') :
            player1.updateFrame("d")
                # Disparar misil para el jugador 1
        if keyboard.is_pressed('c')  and (time.time() - player1.missileTime ) > tiempoRecarga:
            misiles.append(Missile.Missile(player1))
            player1.missileTime = time.time()

        if keyboard.is_pressed('i'):
            player2.avanzar("i", sensibilidad, map)

        if keyboard.is_pressed('k'):
            player2.avanzar("k", sensibilidad, map)

        if keyboard.is_pressed('j') :
            player2.updateFrame("j")

        if keyboard.is_pressed('l') :
            player2.updateFrame("l")
                # Disparar misil para el jugador 2
        if keyboard.is_pressed('n') and (time.time() - player2.missileTime ) > tiempoRecarga:
            misiles.append(Missile.Missile(player2))
            player2.missileTime = time.time()
    
        if keyboard.is_pressed('space'):
            menu = False
            start_time = time.time()  # Inicializa el tiempo cuando se presiona space

        time.sleep(0.03 + sensibilidad)

def main(stdscr):
    global player1, player2, running, menu
    score1 = 0  # Inicializar la puntuación del Jugador 1
    score2 = 0  # Inicializar la puntuación del Jugador 2
    
    # Configura curses
    curses.curs_set(0)  # Oculta el cursor
    stdscr.nodelay(1)   # No bloquea esperando input del usuario
    stdscr.timeout(100) # Refresca cada 100ms

    curses.curs_set(0)  # Oculta el cursor
    stdscr.nodelay(1)  # Hace que getch no bloquee
    stdscr.timeout(100) # Refresca cada 100ms

    # Crear y comenzar el hilo para el teclado
    keyboard_thread = threading.Thread(target=handle_keyboard)
    keyboard_thread.start()
    
    try:
        # Bucle principal


        while running:
            if keyboard.is_pressed('q'):  # Salir con 'q'
                running = False
            
            stdscr.clear()

            while menu:
                stdscr.clear()
                Menu.printMenu(stdscr)
                stdscr.refresh()

            # Calcular el tiempo transcurrido solo si el juego ha comenzado
            if not menu:
                elapsed_time = time.time() - start_time
                if elapsed_time >= game_duration:
                    running = False  # Detener el juego después de 5 minutos
            
            # Mostrar el temporizador en formato ASCII
            print_timer_ascii(stdscr, elapsed_time)  

            player1.print(stdscr)
            player2.print(stdscr)
            map.print(stdscr)

            # Mover y dibujar misiles
            for missile in misiles:
                if missile.collisionWall(map) and not missile.canBounce():
                   misiles.remove(missile)
                 #Comprobar colisiones
                if missile.collisionTank(player2):
                    score1 += 1  # Incrementar el puntaje del jugador 1
                    misiles.remove(missile)  # Eliminar el misil después de la colisión
                elif missile.collisionTank(player1):
                    score2 += 1  # Incrementar el puntaje del jugador 2
                    misiles.remove(missile)  # Eliminar el misil después de la colisión
                missile.move()
                missile.print(stdscr)



            # Mostrar puntuaciones con un desplazamiento de 6 filas hacia abajo
            print_score(stdscr, score1, score2, offset=6)
    
            time.sleep(0.05)
            stdscr.refresh()
    finally:
        running = False  # Ensure the thread stops
        keyboard_thread.join()  # Wait for thread to finish before exiting


# Inicia curses y ejecuta el juego
curses.wrapper(main) 