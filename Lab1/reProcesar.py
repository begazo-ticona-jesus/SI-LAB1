
def reProcesar(ruta):
    sustituciones = {
        'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f',
        'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l',
        'M': 'm', 'N': 'n', 'Ñ': 'ñ', 'O': 'o', 'P': 'p', 'Q': 'q',
        'R': 'r', 'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'X': 'x',
        'Y': 'y', 'Z': 'z'
    }

    with open(ruta, 'r+', encoding='utf-8') as archivo:
        contenido = archivo.read()

        for original, sustitucion in sustituciones.items():
            contenido = contenido.replace(original, sustitucion)
        
        contenido_con_AQP = ''.join([contenido[i:i+20] + "AQP" for i in range(0, len(contenido), 20)])
        print(contenido_con_AQP)
        while len(contenido_con_AQP) % 4 != 0:
            contenido_con_AQP += "X"

        archivo.seek(0)
        archivo.write(contenido_con_AQP)

        archivo.truncate()

    print("reprocesado...")