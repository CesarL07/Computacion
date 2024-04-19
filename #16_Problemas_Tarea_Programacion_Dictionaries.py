#Tarea_Programacion_Dictionaries
print("==============================================================================")
#Ejercicio 1: Multiplicar elementos de un diccionario
Primeros_5_Pares={
    "Primer Numero Par":2,
    "Segundo Numero Par":4,
    "Tercer Numero Par":6,
    "Cuarto Numero Par":8,
    "Quinto Numero Par":10
}
def multiplicar_elementos(dictionarie):
    n=1
    for numero in dictionarie.values():
        n=n*numero
    return n
Res_Prod=multiplicar_elementos(Primeros_5_Pares)
print("El resultado de la multiplicacion es:",Res_Prod)
print("==============================================================================")

#Ejercicio 2: Eliminar una clave de un diccionario
inventario={
    "Producto":"Lapiz",
    "Cantidad":5,
    "Precio":4,
}
def eliminar_key(diccionario,clave):
    if clave in diccionario:
        del diccionario[clave]
    return diccionario
New_Inv=eliminar_key(inventario,"Producto")
print("El inventario con la clave eliminada es:",New_Inv)
print("==============================================================================")

#Ejercicio 3: Convertir dos listas en un diccionario
Peces=["Atun","Tiburon","Barracuda"]
Alimentos=["Lanzones","Tortugas Marinas","Crustaceos"]
diccionario={}
for i in range(len(Peces)):
    diccionario[Peces[i]]=Alimentos[i]
print("El nuevo diccionario sobre peces y su alimentacion es:",diccionario)
print("==============================================================================")

#Ejercicio 4: Ordenar un diccionario dado por clave (orden alfabetico)
Alumnos_Y_Calificaciones={
    "Zatarain":8,
    "Dario":9,
    "Angel":10,
    "Esteban":7
}
New_Dict=dict(sorted(Alumnos_Y_Calificaciones.items()))
print("El nuevo diccionario ordenado alfabeticamente es:",New_Dict)
print("==============================================================================")

#Ejercicio 5: Valores Maximos y Minimos de un diccionario
Valores_Numericos={
    "Numero 1":50,
    "Numero 2":9000,
    "Numero 3":8999,
    "Numero 4":1
}
def Encontrar_Max_Min(diccionario):
    L0=[]
    Lista_Max_Min=[]
    for values in diccionario.values():
        L0.append(values)
    for _ in L0:
        Lista_Max_Min=[max(L0),min(L0)]
    return Lista_Max_Min
print("La lista con los valores maximo y minimo, respectivamente, es:",Encontrar_Max_Min(Valores_Numericos))
print("==============================================================================")

#Ejercicio 6: Obtener un diccionario a partir de los campos de un objeto
class Autos_Ferrari:
    def __init__(self,marca,modelo,precio):
        self.marca=marca
        self.modelo=modelo
        self.precio=precio
    def convertir_a_diccionario(self):
        Dict_Ferrari={
            "marca":self.marca,
            "modelo":self.modelo,
            "precio":self.precio
        }
        return Dict_Ferrari
    def __repr__(self):
     	return "Autos_Ferrari(%s, %s, %s)" % (self.marca, self.modelo, self.precio)
carro=Autos_Ferrari("Ferrari","SF90_Spider","473,000 euros")
print(carro.convertir_a_diccionario())
print("==============================================================================")

#Ejercicio 7: Eliminar elementos duplicados de un diccionario
diccionario_duplicados={
    "Producto1":"Computadora",
    "Producto2":"SmartPhone",
    "Producto3":"Laptop",
    "Producto4":"Computadora"
}
def eliminar_duplicados(diccionario):
    New_Dict2={}
    Values_In_Dict=set()
    for key,value in diccionario.items():
        if value not in Values_In_Dict:
            New_Dict2[key]=value
            Values_In_Dict.add(value)
    return New_Dict2
print("El diccionario sin elementos duplicados es:",eliminar_duplicados(diccionario_duplicados))
print("==============================================================================")

#Ejercicio 8: Verificar si un diccionario esta vacio o no
Dict1={}
Dict2={
    "NOMBRE":"PEPE",
    "ALTURA":1.60
}
def Verificar_si_vacio(diccionario):
    if len(diccionario)==0:
        return True
    else:
        return False
print("¿Es Dict1 un diccionario vacio?",Verificar_si_vacio(Dict1))
print("¿Es Dict2 un diccionario vacio?",Verificar_si_vacio(Dict2))
print("==============================================================================")
       
#Ejercicio 9,10,11: Extraer lista de valores de una lista dada
Diccionario_Original=[
    {'Matematicas': 90, 'ciencia': 92}, 
    {'Matematicas': 89, 'ciencia': 94}, 
    {'Matematicas': 92, 'ciencia': 88}]
#Extraer para la asignatura "Ciencia"
def extraer_calif_ciencia(diccionario,materia):
    Lista_Ciencia=[]
    for calificaciones in diccionario:
        if materia in calificaciones:
            Lista_Ciencia.append(calificaciones[materia])
    return Lista_Ciencia
print("Las calificaciones de ciencia son:",extraer_calif_ciencia(Diccionario_Original,"ciencia"))
#Extraer para la asignatura "Matematicas"
def extraer_calif_matematicas(diccionario,materia):
    Lista_Matematicas=[]
    for calificaciones in diccionario:
        if materia in calificaciones:
            Lista_Matematicas.append(calificaciones[materia])
    return Lista_Matematicas
print("Las calificaciones de matematicas son:",extraer_calif_ciencia(Diccionario_Original,"Matematicas"))
print("==============================================================================")
    
#Ejercicio 12: Encontrar la longitud de un diccionario de valores
Diccionario_Valores={
    "NUM1":1,
    "NUM2":2,
    "NUM3":3
} 
def encontrar_longitud(diccionario):
    longitud_de_diccionario=len(diccionario)
    return longitud_de_diccionario
print("La longitud del diccionario es:",encontrar_longitud(Diccionario_Valores))
print("==============================================================================")

#Ejercicio 13: Encontrar la profundidad de un diccionario 
diccionario_profundidad= {
    "Elemento1": "a",
    "Elemento2": {
        "Sub_Elemento1": "b.1",
        "Sub_Elemento2": {
            "Elemento_subordinado": "c.1.1"
        }
    }
}
def encontrar_profundidad(diccionario):
    if not isinstance(diccionario, dict):
        return 0
    if not diccionario:
        return 1
    max_profundidad=0
    for valor in diccionario.values():
        if isinstance(valor, dict):
            max_profundidad=max(max_profundidad, encontrar_profundidad(valor))
    return 1 + max_profundidad
print("La profundidad del diccionario es",encontrar_profundidad(diccionario_profundidad))
print("==============================================================================")

#Ejercicio 14: Acceder al elemento de un diccionario por indice
#No entendi correctamente este problema, busque un poco de ayuda y lo interprete de la siguiente manera
#Se utilizan las keys del diccionario como indices para acceder a su elemento/valor correspondiente, el cual se imprime
dict_materias={
    "fisica": 10,
    "matemáticas": 8,
    "química": 6
}
Lista_materias=[]
for materia in dict_materias.keys():
    Lista_materias.append(materia)

for indice in range(len(Lista_materias)):
    print(dict_materias[Lista_materias[indice]])
print("==============================================================================")

#Ejercicio 15: Convertir un diccionario en una lista de listas
Diccio_original = {1: 'rojo', 2: 'verde', 3: 'negro', 4: 'blanco', 5: 'negro'}
Lista_de_Listas=[]
for key,value in Diccio_original.items():
    Lista_de_Listas.append([key,value])
print("La lista de listas generada es:",Lista_de_Listas)
print("==============================================================================")

#Ejercicio 16: Filtrar numeros pares de un diccionario de valores
Diccionario_de_Valores1={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
Diccionario_de_Valores2={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}

def Filtrar_Pares(diccionario):
    diccionario_filtrado={}
    for key,value in diccionario.items():
        valores_filtrados=[]
        for numero in value:
            if numero%2==0:
                valores_filtrados.append(numero)
                diccionario_filtrado[key]=valores_filtrados
    return diccionario_filtrado
print("El Diccionario_de_Valores1 filtrado es:",Filtrar_Pares(Diccionario_de_Valores1))
print("El Diccionario_de_Valores1 filtrado es:",Filtrar_Pares(Diccionario_de_Valores2))

print("==============================================================================")





