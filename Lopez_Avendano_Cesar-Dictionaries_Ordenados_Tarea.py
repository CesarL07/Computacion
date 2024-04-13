#Dictionaries_Tarea1_Nombres-Ordenados
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

nombres_ordenados=dict(sorted(students_in_math.items()))
for key,value in nombres_ordenados.items():
    print("El/La alumno(a):",key,",tiene una calificacion de",value)



