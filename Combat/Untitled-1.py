import Sprites

prefijo = "pOne_f"
for n in range(24):
    frame = Sprites.Frames("Player1").getFrame(n)
    coordenadas = []
    lines = frame.strip().splitlines()

    for i, line in enumerate(lines):
        coordenadas.append([])
        for j, char in enumerate(line):
            if char == "$":
                coordenadas[i].append(j)

    print(prefijo + str(n) + " = [")
    for i in range(len(coordenadas)):
        if i < len(coordenadas)-1:
            print(str(coordenadas[i]) + ",")
        else:
            print(coordenadas[i])
    print("]")
    print ("\n")