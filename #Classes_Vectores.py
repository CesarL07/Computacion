#Classes_Python_Vectores
import math
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
        
    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
        
    def prod_escalar(self, escalar):
        return Vector3D(self.x * escalar, self.y * escalar, self.z * escalar)
    
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
        
    def pcross(self,other):
        return Vector3D(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)
	
    def norma(self):
     	return round(math.sqrt((self.x*self.x)+(self.y*self.y)+(self.z*self.z)),2)  
     	
    def angulo_vectores(self,other):
        return round(math.acos(self*other/((self.norma()*other.norma())))*(180/math.pi),0) 
    
    def triple_producto_Escalar(self,Vec1,Vec2):
        return ((self.x * (Vec1.y * Vec2.z - Vec1.z * Vec2.y)) + (self.y * (Vec1.z * Vec2.x - Vec1.x * Vec2.z)) + (self.z * (Vec1.x * Vec2.y - Vec1.y * Vec2.x)))        

    def triple_producto_Vectorial(self,Vec1,Vec2):
        prod_vectorial=Vector3D(Vec1.y * Vec2.z - Vec1.z * Vec2.y, Vec1.z * Vec2.x - Vec1.x * Vec2.z, Vec1.x * Vec2.y - Vec1.y * Vec2.x)
        t_p_v=Vector3D(self.y * prod_vectorial.z - self.z * prod_vectorial.y, self.z * prod_vectorial.x - self.x * prod_vectorial.z, self.x * prod_vectorial.y - self.y * prod_vectorial.x)
        return t_p_v
    
    def comparar_igualdad(self,other):
        if self.x==other.x and self.y==other.y and self.z==other.z:
            return True
        else:
            return False
    
    def agregar_vector(self):
        while True:
            try:
                comp_X = float(input("Introduzca el valor de la componente i: "))
                comp_Y = float(input("Introduzca el valor de la componente j: "))
                comp_Z = float(input("Introduzca el valor de la componente k: "))
                return Vector3D(comp_X, comp_Y, comp_Z)
            except ValueError:
                print("Por favor, introduzca valores validos para las componentes del vector.")
    
    def __repr__(self):
    	#return f"Vector3D({self.x},{self.y},{self.z})"
     	return "VECTOR3D(%s, %s, %s)" % (self.x, self.y, self.z)
    

V1=Vector3D(1,2,3)
V2=Vector3D(5,6,7)
V3=Vector3D(1,0,0)
V4=Vector3D(0,1,0)

VN1=Vector3D(3,1,1)
VN2=Vector3D(0,0,6)
VN3=Vector3D(0,7,0)

VNI1=Vector3D(0,0,1)
VNI2=Vector3D(1,0,0)

VI1=Vector3D(2,2,2)
VI2=Vector3D(2,2,2)

sum_result = V1 + V2
print("La suma de vectores es:",sum_result)

cruz=V1.pcross(V2)
print("El producto cruz es:",cruz)

magnitud=V1.norma()
print("La norma del vector es:",magnitud)

angulo=V3.angulo_vectores(V4)
print ("El angulo entre los vectores es:",angulo)

prod_triple_escalar=VN1.triple_producto_Escalar(VN2,VN3)
print("El triple producto escalar es:",prod_triple_escalar)

prod_triple_vectorial=VN1.triple_producto_Vectorial(VN2,VN3)
print("El triple producto vectorial es:",prod_triple_vectorial)

vectores_no_iguales=VNI1.comparar_igualdad(VNI2)
print("Se verifica la igualdad:",vectores_no_iguales)
igualdad_de_vectores=VI1.comparar_igualdad(VI2)
print("Se verifica la igualdad:",igualdad_de_vectores)

VectorExistente=Vector3D(5,5,5)
nuevo_vector=VectorExistente.agregar_vector()
print("El vector agregado es:",nuevo_vector)
