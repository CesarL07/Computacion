#Tarea Clase Heredada

#Este codigo verifica que el tipo de entrada sea correcta, identifica cuando sucede un error y permite reingresar 
#el dato correspondiente. Verifique al modificar las datos en la parte final del codigo.

class EstudiantesUAS:
    def __init__(self, nombre, carrera, anio, num_cuenta):
        while True:
            try:
                if not isinstance(nombre, str):
                    raise TypeError("El nombre debe ser texto")
                self.nombre = nombre
                
                if not isinstance(carrera, str):
                    raise TypeError("La carrera debe ser texto")
                self.carrera = carrera
                
                if not isinstance(anio, int):
                    raise TypeError("El año debe ser un número entero")
                self.anio = anio
                
                if not isinstance(num_cuenta, int):
                    raise TypeError("El número de cuenta debe ser un número entero")
                self.num_cuenta = num_cuenta
                break  
            except TypeError as __:
                print(__)
                if "nombre" in str(__):
                    nombre = input("Ingrese nuevamente el nombre: ")
                elif "carrera" in str(__):
                    carrera = input("Ingrese nuevamente la carrera: ")
                elif "año" in str(__):
                    anio = int(input("Ingrese nuevamente el año: "))
                elif "cuenta" in str(__):
                    num_cuenta = int(input("Ingrese nuevamente el número de cuenta: "))
        
    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Carrera:{self.carrera}, Año:{self.anio}, Numero_de_cuenta:{self.num_cuenta}"

class EstudiantesFisica(EstudiantesUAS):
    def __init__(self, nombre, carrera, anio, num_cuenta, laboratorio):
        super().__init__(nombre, carrera, anio, num_cuenta)
        while True:
            try:
                if not isinstance(laboratorio, str):
                    raise TypeError("El laboratorio debe ser texto")
                self.laboratorio = laboratorio
                break
            except TypeError as __:
                print(__)
                laboratorio = input("Ingrese nuevamente el laboratorio: ")
    
    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, Laboratorio: {self.laboratorio}"
    
class EstudiantesMatematicas(EstudiantesUAS):
    def __init__(self, nombre, carrera, anio, num_cuenta, software_matematico):
        super().__init__(nombre, carrera, anio, num_cuenta)
        while True:
            try:
                if not isinstance(software_matematico, str):
                    raise TypeError("El software debe ser texto")
                self.software_matematico = software_matematico
                break
            except TypeError as __:
                print(__)
                software_matematico = input("Ingrese nuevamente el software que usa: ")

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, Software que usa: {self.software_matematico}"

class EstudiantesElectronica(EstudiantesUAS):
    def __init__(self, nombre, carrera, anio, num_cuenta, materiales):
        super().__init__(nombre, carrera, anio, num_cuenta)
        while True:
            try:
                if not isinstance(materiales, str):
                    raise TypeError("Los materiales deben ser texto")
                self.materiales = materiales
                break
            except TypeError as __:
                print(__)
                materiales = input("Ingrese nuevamente los materiales de uso: ")

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, Materiales de uso: {self.materiales}"


print("==============================================================================")

alumno1_fisica = EstudiantesFisica("Luis", "Fisica", 1, 77777777, "Laboratorio de optica")
alumno2_fisica = EstudiantesFisica("Manuel", "Fisica", 3, 88888888, "Laboratorio de materiales")
alumno3_fisica = EstudiantesFisica("Pepe", "Fisica", 4, 99999999, "Laboratorio de cuantica")
alumno4_fisica = EstudiantesFisica("Pedro", "Fisica", 2, 10101010, "Laboratorio de sintesis")

print(alumno1_fisica.mostrar_info())
print(alumno2_fisica.mostrar_info())
print(alumno3_fisica.mostrar_info())
print(alumno4_fisica.mostrar_info())

print("==============================================================================")

alumno1_matematicas = EstudiantesMatematicas("Maria", "Matematicas", 3, 11111111, "Mathlab")
alumno2_matematicas = EstudiantesMatematicas("Karolina", "Matematicas", 5, 22222222, "Mathematica")
alumno3_matematicas = EstudiantesMatematicas("Ruiz", "Matematicas", 2, 33333333, "Maple")

print(alumno1_matematicas.mostrar_info())
print(alumno2_matematicas.mostrar_info())
print(alumno3_matematicas.mostrar_info())

print("==============================================================================")

alumno1_electronica = EstudiantesElectronica("Felipe", "Electronica", 6, 44444444, "Fuentes de energia")
alumno2_electronica = EstudiantesElectronica("Daniel", "Electronica", 1, 55555555, "Placas de circuito")
alumno3_electronica = EstudiantesElectronica("Javier", "Electronica", 4, 66666666, "Osciloscopios")

print(alumno1_electronica.mostrar_info())
print(alumno2_electronica.mostrar_info())
print(alumno3_electronica.mostrar_info())

print("==============================================================================")
