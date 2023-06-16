import frecuencias
import trigramas
import eliminar_espacios
import eliminar_tildes
import mayuscula
import reProcesar
import sustituciones
ruta_archivo = 'POEMA_PRE.txt'


sustituciones.sustituir(ruta_archivo)
eliminar_tildes.elimninarTildes(ruta_archivo)
eliminar_espacios.eliminarEspacios(ruta_archivo)
mayuscula.mayusculas(ruta_archivo)

dic_frecuencia = frecuencias.frecuencias(ruta_archivo)
print(dic_frecuencia)
    
ordenamiento = sorted(dic_frecuencia.items(), key=lambda x: x[1], reverse=True)
mayor_frecuencia = ordenamiento[:5]
print(mayor_frecuencia)

lista_trigramas = trigramas.encontrar_trigramas(ruta_archivo)
lista_distancias = trigramas.encontrar_distancias(ruta_archivo)
print(lista_distancias)

reProcesar.reProcesar(ruta_archivo)


