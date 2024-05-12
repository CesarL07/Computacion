#Tarea - Configurar-Histograma
import numpy as np
import random as random
import matplotlib.pyplot as plt

lista=[]
for i in range(0,50):
    valores=round(random.random(),2)
    lista.append(valores)

bins=np.linspace(0,1,10)
plt.hist(lista, bins=bins, edgecolor='black') #Con esto grafico el histograma
plt.xlabel("valor")  
plt.ylabel("Frecuencia") 
plt.title("Histograma")  
plt.grid(True)  
plt.show() 

rango1=[]
rango2=[]
rango3=[]
rango4=[] 
rango5=[]
rango6=[]
rango7=[]
rango8=[] 
rango9=[]  
rango10=[]
for x in lista:
    if 0.00<=x<=0.10:
        rango1.append(x)
    elif 0.10<x<=0.20:
        rango2.append(x)
    elif 0.20<x<=0.30:
        rango3.append(x)
    elif 0.30<=x<=0.40:
        rango4.append(x)
    elif 0.40<x<=0.50:
        rango5.append(x)
    elif 0.50<x<=0.60:
        rango6.append(x)
    elif 0.60<=x<=0.70:
        rango7.append(x)
    elif 0.70<x<=0.80:
        rango8.append(x)
    elif 0.80<x<=0.90:
        rango9.append(x)
    elif 0.90<x<=1.00:
        rango10.append(x)
lista_listas=[rango1,rango2,rango3,rango4,rango5,rango6,rango7,rango8,rango9,rango10]
print(lista_listas) #Esta es una lista de listas que contiene los valores generados en su respectivo rango


