#Tarea Graficar Parábola
#Para este código se asume que en el tiro parabólico, el tiempo de subida es el mismo que el de bajada
import math
import turtle as t

def dibujar_ejes():
    #Con este ciclo dibujo al eje "y" y sus correspondientes valores
    t.penup()
    t.goto(0, -350)
    t.pendown()
    t.goto(0, 350)
    for i in range(-350, 350, 40):
        t.penup()
        t.goto(-20, i)
        t.pendown()
        t.write(str(i))

    #Con este otro dibujo al eje "x" y sus correspondientes valores
    t.penup()
    t.goto(-620, 0)
    t.pendown()
    t.goto(620, 0)
    for i in range(-620, 620, 40):
        t.penup()
        t.goto(i, -15)
        t.pendown()
        t.write(str(i))

def parabola(pos_ini,vi,ang):
    t.pu()
    t.speed(0)

    xi,yi=pos_ini
    g=9.81
    v1x=vi*math.cos((ang*math.pi)/180)
    v1y=vi*math.sin((ang*math.pi)/180)
    t_vuelo=(2*v1y)/g
    puntos_totales=100
    t_por_punto=t_vuelo/puntos_totales

    t.setpos(xi,yi)
    t.pd()

    for i in range(101):
        xf=xi+v1x*i*t_por_punto
        yf=yi+(v1y*i*t_por_punto)-((1/2)*g*((i*t_por_punto)**2))
        t.setpos(xf,yf)
    t.mainloop()

pi=(-620,0)
vi=110
ang=45
dibujar_ejes()
parabola(pi,vi,ang)
