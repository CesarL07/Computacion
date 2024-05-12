#Tarea Graficar Parabola
#Para este codigo se asume que en el tiro parabolico, el tiempo de subida es el mismo que el de bajada
import math
import turtle as t

def parabola(pos_ini,vi,ang):
    t.pu()
    t.speed(0)

    xi,yi=pos_ini
    g=9.81
    v1x=vi*math.cos((ang*math.pi)/180)
    v1y=vi*math.sin((ang*math.pi)/180)
    t_vuelo=(2*v1y)/g
    puntos_totales=10
    t_por_punto=t_vuelo/puntos_totales

    t.setpos(xi,yi)
    t.pd()

    for i in range(11):
        xf=xi+v1x*i*t_por_punto
        yf=yi+(v1y*i*t_por_punto)-((1/2)*g*((i*t_por_punto)**2))
        t.setpos(xf,yf)
        print(xf,yf)
    t.mainloop()

pi=(-620,0)
vi=110
ang=45

parabola(pi,vi,ang)