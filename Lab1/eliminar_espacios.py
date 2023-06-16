
def eliminarEspacios(ruta):
    sustituciones = {
        ' ': '',
        '!': '',
        '¡': '',
        '¿': '',
        '?': '',
        '.': '',
        ',': '',
        ';': '',
        ':': '',
        '\n':''
    }

    with open(ruta, 'r+', encoding='utf-8') as archivo:
        contenido = archivo.read()
        print(contenido)

        for original, sustitucion in sustituciones.items():
            contenido = contenido.replace(original, sustitucion)

        archivo.seek(0)
        archivo.write(contenido)

        archivo.truncate()

        archivoNuevo = open("POEMA_PRE.txt", "w")
        archivoNuevo.write(contenido)
        archivoNuevo.close()
    print("poema pre...")