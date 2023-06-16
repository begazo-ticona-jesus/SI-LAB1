salida_archivo = 'poema.txt'
def elimninarTildes(ruta):
    sustituciones = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
        'Á': 'A',
        'É': 'E',
        'Í': 'I',
        'Ó': 'O',
        'Ú': 'U'
    }

    with open(ruta, 'r+', encoding='utf-8') as archivo:
        contenido = archivo.read()
        print(contenido)

        for original, sustitucion in sustituciones.items():
            contenido = contenido.replace(original, sustitucion)

        archivo.seek(0)
        archivo.write(contenido)

        archivo.truncate()

    print("Tildes Eliminadas...")