def frecuencias(archivo):
    frecuencias_letras = {}

    with open(archivo, 'r') as txt:
        contenido = txt.read()

        for letra in range(ord('A'), ord('Z')+1):
            # Obtener el carácter correspondiente a la letra
            letra = chr(letra)
            # Calcular la frecuencia de la letra en el contenido del archivo
            frecuencia = contenido.count(letra)
            # Agregar la letra y su frecuencia al diccionario
            frecuencias_letras[letra] = frecuencia

    return frecuencias_letras
