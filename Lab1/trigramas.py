def encontrar_trigramas(archivo):
    with open(archivo, "r") as archivo_preprocesado:
        texto = archivo_preprocesado.read()
        trigramas = []
        for i in range(len(texto) - 2):
            trigrama = texto[i:i+3]
            trigramas.append(trigrama)
        return trigramas

def encontrar_distancias(archivo):
    with open(archivo, "r") as archivo_preprocesado:
        texto = archivo_preprocesado.read()
        distancias = []
        trigramas_previos = {}
        
        for i in range(len(texto) - 2):
            trigrama = texto[i:i+3]
            
            if trigrama in trigramas_previos:
                distancia = i - trigramas_previos[trigrama]
                distancias.append(distancia)
            
            trigramas_previos[trigrama] = i
        
        return distancias