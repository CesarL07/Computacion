#Tarea Clase Heredada

class EstudiantesUAS:
    def __init__(self,nombre,carrera,anio,num_cuenta):
        self.nombre=nombre
        self.carrera=carrera
        self.anio=anio
        self.num_cuenta=num_cuenta
    
    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Carrera:{self.carrera}, Año:{self.anio}, Numero_de_cuenta:{self.num_cuenta}"

class EstudiantesFisica(EstudiantesUAS):
    def __init__(self,nombre,carrera,anio,num_cuenta,laboratorio):
        super().__init__(nombre,carrera,anio,num_cuenta)
        self.laboratorio=laboratorio
    
    def mostrar_info(self):
        info_base=super().mostrar_info()
        return f"{info_base}, Laboratorio:{self.laboratorio}"
    
class EstudiantesMatematicas(EstudiantesUAS):
    def __init__(self,nombre,carrera,anio,num_cuenta,software_matematico):
        super().__init__(nombre,carrera,anio,num_cuenta)
        self.software_matematico=software_matematico

    def mostrar_info(self):
        info_base=super().mostrar_info()
        return f"{info_base}, Software_que_usa:{self.software_matematico}"

class EstudiantesElectronica(EstudiantesUAS):
    def __init__(self,nombre,carrera,anio,num_cuenta,materiales):
        super().__init__(nombre,carrera,anio,num_cuenta)
        self.materiales=materiales

    def mostrar_info(self):
        info_base=super().mostrar_info()
        return f"{info_base}, Materiales_de_uso:{self.materiales}"

print("==============================================================================")

alumno1_fisica=EstudiantesFisica("Luis","Fisica",1,11112222,"Laboratorio de optica")
alumno2_fisica=EstudiantesFisica("Manuel","Fisica",3,33334444,"Laboratorio de materiales")
alumno3_fisica=EstudiantesFisica("Pepe","Fisica",4,55556666,"Laboratorio de cuantica")
alumno4_fisica=EstudiantesFisica("Pedro","Fisica",2,77778888,"Laboratorio de sintesis")

print(alumno1_fisica.mostrar_info())
print(alumno2_fisica.mostrar_info())
print(alumno3_fisica.mostrar_info())
print(alumno4_fisica.mostrar_info())

print("==============================================================================")

alumno1_matematicas=EstudiantesMatematicas("Maria","Matematicas",1,11112222,"Mathlab")
alumno2_matematicas=EstudiantesMatematicas("Karolina","Matematicas",3,33334444,"Mathematica")
alumno3_matematicas=EstudiantesMatematicas("Ruiz","Matematicas",4,55556666,"Maple")

print(alumno1_matematicas.mostrar_info())
print(alumno2_matematicas.mostrar_info())
print(alumno3_matematicas.mostrar_info())

print("==============================================================================")

alumno1_electronica=EstudiantesMatematicas("Felipe","Electronica",1,11112222,"Fuentes de energia")
alumno2_electronica=EstudiantesMatematicas("Daniel","Electronica",3,33334444,"Placas de circuito")
alumno3_electronica=EstudiantesMatematicas("Javier","Electronica",4,55556666,"Osciloscopios")

print(alumno1_electronica.mostrar_info())
print(alumno2_electronica.mostrar_info())
print(alumno3_electronica.mostrar_info())

print("==============================================================================")
