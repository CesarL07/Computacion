#Tarea - Lista de listas-Import.txt
#Este codigo crea una lista de listas, donde cada lista individual es conformada por los elementos de cada linea de los elementos de un txt
import time

lista_de_listas=[]
with open("archivo.txt","r",encoding="utf-8") as archivo:
    for linea in archivo:
        linea_individual=linea.strip().split()
        lista_de_listas.append([linea_individual])

print(f"La lista de listas resultantes es: {lista_de_listas}")
