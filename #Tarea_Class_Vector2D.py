#Tarea_class_VECTOR2D
import math

class Vector2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def suma_vectores(self,other):
        return Vector2D(self.x+other.x, self.y+other.y)
    
    def resta_vectores(self,other):
        return Vector2D(self.x-other.x, self.y-other.y)
    
    def multiplicar_escalar(self,scalar):
        return Vector2D(self.x*scalar, self.y*scalar)

    def producto_punto(self,other):
        return (self.x*other.x + self.y*other.y)

    def norma(self):
        return (round(math.sqrt(self.x**2 + self.y**2)))

    #Originalmente realice unicamente las instrucciones marcadas como comentarios.
    #Ante la posibilidad de un error de rango, implemento esto primero, pero decidi conservar el anterior procedimiento
    def angulo_entre_vectores(self,other):
        producto_punto1 = self.producto_punto(other)
        magnitud1=self.norma()
        magnitud2=other.norma()
        argumento_acos=producto_punto1/(magnitud1*magnitud2)
        argumento_acos=max(min(argumento_acos,1.0),-1.0)
        angulo_radianes=math.acos(argumento_acos)
        angulo_grados=round(angulo_radianes*(180/math.pi),2)
        return angulo_grados
        #producto_punto_2 = self.producto_punto(other)
        #norma1 = self.norma()
        #norma2 = other.norma()
        #producto_norma_2 = norma1 * norma2
        #return round(math.acos(producto_punto_2 / producto_norma_2) * (180 / math.pi), 2)
        
    def unitario_x():
        return Vector2D(1,0)
    def unitario_y():
        return Vector2D(0,1)

    def angulo_eje_x(self):
        unitario_x=Vector2D.unitario_x()
        producto_punto1=self.producto_punto(unitario_x)
        norma1=self.norma()
        norma2=unitario_x.norma()
        argumento_acos=producto_punto1/(norma1*norma2)
        argumento_acos = max(min(argumento_acos, 1.0), -1.0)
        angulo_radianes = math.acos(argumento_acos)
        angulo_grados = round(angulo_radianes * (180 / math.pi), 2)
        return angulo_grados
    
    def angulo_eje_y(self):
        unitario_y=Vector2D.unitario_y()
        producto_punto1=self.producto_punto(unitario_y)
        norma1=self.norma()
        norma2=unitario_y.norma()
        argumento_acos=producto_punto1/(norma1*norma2)
        argumento_acos = max(min(argumento_acos, 1.0), -1.0)
        angulo_radianes = math.acos(argumento_acos)
        angulo_grados = round(angulo_radianes * (180 / math.pi), 2)
        return angulo_grados
    
    def proyeccion_v1_sobre_v2(self,other):
        v1=self
        v2=other
        producto_punto1=v1.producto_punto(v2)
        magnitud_v2=v2.norma()**2
        factor=producto_punto1/magnitud_v2
        proyeccion_x=round(factor*other.x,2)
        proyeccion_y=round(factor*other.y,2)
        return Vector2D(proyeccion_x,proyeccion_y)

    def __repr__(self):
     	return "VECTOR2D(%s, %s)" % (self.x, self.y)
    
v1=Vector2D(0,1)
v2=Vector2D(2,1)    

V1=Vector2D(2,-3)
V2=Vector2D(-9,6)

print("==================================================")
suma_vectores=v1.suma_vectores(v2)
print("La suma de los vectores es:",suma_vectores)
print("==================================================")
resta_vectores=v1.resta_vectores(v2)
print("La resta de los vectores es:",resta_vectores)
print("==================================================")
producto_por_escalar=v1.multiplicar_escalar(5)
print("El vector multiplicado por el escalar dado es:",producto_por_escalar)
print("==================================================")
producto_punto=v1.producto_punto(v2)
print("El producto punto de los vectores dados es:",producto_punto)
print("==================================================")
norma_vector=v1.norma()
print("La norma del vector dado es:",norma_vector)
print("==================================================")
angulo_entre_vectores=v1.angulo_entre_vectores(v2)
print("El angulo entre los vectores dados es:",angulo_entre_vectores)
print("==================================================")
angulo_respecto_eje_x=v1.angulo_eje_x()
print("El angulo con respecto al eje x del vector dado es:",angulo_respecto_eje_x)
print("==================================================")
angulo_respecto_eje_y=v1.angulo_eje_y()
print("El angulo con respecto al eje y del vector dado es:",angulo_respecto_eje_y)
print("==================================================")
proyeccion=V1.proyeccion_v1_sobre_v2(V2)
print("La proyeccion de los vectores dados es:",proyeccion)