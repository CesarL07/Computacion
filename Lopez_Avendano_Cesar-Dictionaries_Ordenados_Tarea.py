#Dictionaries_Tarea1
students_in_math={
    "Jael":8,
    "Jose":7,   
    "Derek":9,
    "René":10,
    "Manuel":9,
    "Guillermo":8,
    "Angel":10,
    "Santiago":9,
    "Said":7,
    "Ana":10,
    "Carolina":9    
}
for key,value in students_in_math.items():
    print("El/La alumno(a):",key,",tiene una calificacion de:",value)
print("===================================================")

# Imprimir el diccionario ordenado por orden alfabetico
nombres_ordenados=dict(sorted(students_in_math.items()))
for key,value in nombres_ordenados.items():
    print("El/La alumno(a):",key,",tiene una calificacion de",value)
print("====================================================")

# Imprimir el diccionario ordenado por orden numerico (calificaciones)
calificaciones_ordenadas=sorted(students_in_math, key=students_in_math.get, reverse=True)
for alumno in calificaciones_ordenadas:
    print("El/La alumno(a):",alumno,"tiene una calificacion de",str(students_in_math[alumno]))



