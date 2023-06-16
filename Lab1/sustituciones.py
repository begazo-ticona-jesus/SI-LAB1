
def sustituir(ruta):
    sustituciones = {
        'a': 'o',
        'h': 'i',
        'ñ': 'm',
        'k': 'l',
        'u': 'v',
        'w': 'v',
        'z': 'y',
        'x': 'r',
        'A': 'o',
        'H': 'i',
        'Ñ': 'm',
        'K': 'l',
        'U': 'v',
        'W': 'v',
        'Z': 'y',
        'X': 'r'
    }

    # Abrir el archivo en modo lectura y lectura/escritura
    with open(ruta, 'r+', encoding='utf-8') as archivo:
        contenido = archivo.read()

        # Realizar las sustituciones
        for original, sustitucion in sustituciones.items():
            contenido = contenido.replace(original, sustitucion)

        # ir al inicio del archivo
        archivo.seek(0)
        archivo.write(contenido)

        # Truncar el contenido restante en caso de que el archivo original fuera más largo
        archivo.truncate()

    print("Suistituido...")