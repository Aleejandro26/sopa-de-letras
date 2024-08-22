import random

def crear_sopa_de_letras(tamaño, palabras):
    # Inicializar la sopa de letras con espacios
    sopa = [[' ' for _ in range(tamaño)] for _ in range(tamaño)]
    
    def colocar_palabra(palabra):
        longitud = len(palabra)
        direccion = random.choice(['horizontal', 'vertical', 'diagonal'])
        
        if direccion == 'horizontal':
            fila = random.randint(0, tamaño - 1)
            columna = random.randint(0, tamaño - longitud)
            for i in range(longitud):
                if sopa[fila][columna + i] in (' ', palabra[i]):
                    sopa[fila][columna + i] = palabra[i]
                else:
                    return False
        elif direccion == 'vertical':
            fila = random.randint(0, tamaño - longitud)
            columna = random.randint(0, tamaño - 1)
            for i in range(longitud):
                if sopa[fila + i][columna] in (' ', palabra[i]):
                    sopa[fila + i][columna] = palabra[i]
                else:
                    return False
        elif direccion == 'diagonal':
            fila = random.randint(0, tamaño - longitud)
            columna = random.randint(0, tamaño - longitud)
            for i in range(longitud):
                if sopa[fila + i][columna + i] in (' ', palabra[i]):
                    sopa[fila + i][columna + i] = palabra[i]
                else:
                    return False
        return True

    # Colocar palabras en la sopa
    for palabra in palabras:
        colocado = False
        while not colocado:
            colocado = colocar_palabra(palabra)
    
    # Rellenar los espacios vacíos con letras aleatorias
    for i in range(tamaño):
        for j in range(tamaño):
            if sopa[i][j] == ' ':
                sopa[i][j] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    return sopa

def imprimir_sopa_de_letras(sopa):
    for fila in sopa:
        print(' '.join(fila))

def jugar_sopa_de_letras(sopa, palabras):
    palabras_encontradas = []
    
    while len(palabras_encontradas) < len(palabras):
        imprimir_sopa_de_letras(sopa)
        print("\nPalabras por encontrar:")
        print(', '.join(palabras))
        palabra = input("Ingrese una palabra para buscar: ").upper()
        
        if palabra in palabras:
            if palabra in palabras_encontradas:
                print("¡Ya has encontrado esta palabra!")
            else:
                print(f"¡Palabra '{palabra}' encontrada!")
                palabras_encontradas.append(palabra)
        else:
            print("Palabra no válida o ya encontrada.")
        
        if len(palabras_encontradas) == len(palabras):
            print("¡Felicidades! Has encontrado todas las palabras.")
        else:
            print(f"Palabras encontradas: {', '.join(palabras_encontradas)}")
    
if __name__ == "__main__":
    tamaño = 10
    palabras = ['PYTHON', 'CODIGO', 'CONSOLAS', 'JUEGO', 'DESAFIO']
    
    sopa = crear_sopa_de_letras(tamaño, palabras)
    jugar_sopa_de_letras(sopa, palabras)
