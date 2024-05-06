#Tarea Clase Heredada

class EstudiantesUAS:
    def __init__(self,nombre,carrera,anio,num_cuenta):
        self.verificar_nombre(nombre)
        self.nombre=nombre
        self.verificar_carrera(carrera)
        self.carrera=carrera
        self.verificar_anio(anio)
        self.anio=anio
        self.verificar_cuenta(num_cuenta)
        self.num_cuenta=num_cuenta

    def verificar_nombre(self,texto):
        if not isinstance(texto,str):
            raise TypeError("El nombre debe ser texto")
    
    def verificar_carrera(self,texto):
        if not isinstance(texto,str):
            raise TypeError("La carrera debe ser texto")
    
    def verificar_anio(self,numero):
        if not isinstance(numero,int):
            raise TypeError("El año es un numero")

    def verificar_cuenta(self,numero):
        if not isinstance(numero,int):
            raise TypeError("El numero de cuenta son solo numeros")
        
    def verificar_laboratorio(self,texto):
        if not isinstance(texto,str):
            raise TypeError("El laboratorio debe ser texto")
    
    def verificar_software(self,texto):
        if not isinstance(texto,str):
            raise TypeError("El software debe ser texto")
        
    def verificar_materiales(self,texto):
        if not isinstance(texto,str):
            raise TypeError("Los materiales deben ser texto")
        
    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Carrera:{self.carrera}, Año:{self.anio}, Numero_de_cuenta:{self.num_cuenta}"

class EstudiantesFisica(EstudiantesUAS):
    def __init__(self,nombre,carrera,anio,num_cuenta,laboratorio):
        super().__init__(nombre,carrera,anio,num_cuenta)
        self.verificar_laboratorio(laboratorio)
        self.laboratorio=laboratorio
    
    def mostrar_info(self):
        info_base=super().mostrar_info()
        return f"{info_base}, Laboratorio:{self.laboratorio}"
    
class EstudiantesMatematicas(EstudiantesUAS):
    def __init__(self,nombre,carrera,anio,num_cuenta,software_matematico):
        super().__init__(nombre,carrera,anio,num_cuenta)
        self.verificar_software(software_matematico)
        self.software_matematico=software_matematico

    def mostrar_info(self):
        info_base=super().mostrar_info()
        return f"{info_base}, Software_que_usa:{self.software_matematico}"

class EstudiantesElectronica(EstudiantesUAS):
    def __init__(self,nombre,carrera,anio,num_cuenta,materiales):
        super().__init__(nombre,carrera,anio,num_cuenta)
        self.verificar_materiales(materiales)
        self.materiales=materiales

    def mostrar_info(self):
        info_base=super().mostrar_info()
        return f"{info_base}, Materiales_de_uso:{self.materiales}"

print("==============================================================================")

alumno1_fisica=EstudiantesFisica("Luis","Fisica",1,77777777,"Laboratorio de optica")
alumno2_fisica=EstudiantesFisica("Manuel","Fisica",3,88888888,"Laboratorio de materiales")
alumno3_fisica=EstudiantesFisica("Pepe","Fisica",4,99999999,"Laboratorio de cuantica")
alumno4_fisica=EstudiantesFisica("Pedro","Fisica",2,10101010,"Laboratorio de sintesis")

print(alumno1_fisica.mostrar_info())
print(alumno2_fisica.mostrar_info())
print(alumno3_fisica.mostrar_info())
print(alumno4_fisica.mostrar_info())

print("==============================================================================")

alumno1_matematicas=EstudiantesMatematicas("Maria","Matematicas",3,11111111,"Mathlab")
alumno2_matematicas=EstudiantesMatematicas("Karolina","Matematicas",5,22222222,"Mathematica")
alumno3_matematicas=EstudiantesMatematicas("Ruiz","Matematicas",2,33333333,"Maple")

print(alumno1_matematicas.mostrar_info())
print(alumno2_matematicas.mostrar_info())
print(alumno3_matematicas.mostrar_info())

print("==============================================================================")

alumno1_electronica=EstudiantesElectronica("Felipe","Electronica",6,44444444,"Fuentes de energia")
alumno2_electronica=EstudiantesElectronica("Daniel","Electronica",1,55555555,"Placas de circuito")
alumno3_electronica=EstudiantesElectronica("Javier","Electronica",4,66666666,"Osciloscopios")

print(alumno1_electronica.mostrar_info())
print(alumno2_electronica.mostrar_info())
print(alumno3_electronica.mostrar_info())

print("==============================================================================")
