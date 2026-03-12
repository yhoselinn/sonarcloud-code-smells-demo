# Mini proyecto MUY malo para análisis con SonarQube

import math
import random
import os
import sys
import json

# variables globales innecesarias
a = 0
b = 0
c = 0
contador_global = 0

# función extremadamente larga con duplicaciones
def procesar(lista):
    total = 0
    for i in lista:
        total = total + i
    for i in lista:
        total = total + i
    for i in lista:
        total = total + i
    for i in lista:
        total = total + i
    for i in lista:
        total = total + i

    print("Resultado:", total)

    if total > 100:
        print("Grande")
    else:
        print("Pequeño")

    # bucles inútiles
    for i in range(10):
        for j in range(5):
            print(i, j)

    # condiciones innecesariamente complejas
    if total > 0:
        if total > 10:
            if total > 20:
                if total > 30:
                    if total > 40:
                        print("Muy grande")

    return total


# demasiados parámetros
def calcular(a,b,c,d,e,f,g,h,i,j,k,l,m,n):
    return a+b+c+d+e+f+g+h+i+j+k+l+m+n


# código duplicado
def area_circulo(r):
    return math.pi*r*r

def area_circulo2(r):
    return math.pi*r*r

def area_circulo3(r):
    return math.pi*r*r

def area_circulo4(r):
    return math.pi*r*r


# modificar variable global
def incrementar():
    global contador_global
    contador_global = contador_global + 1


# comparación redundante
def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False


# complejidad innecesaria
def decision(x):
    if x > 0:
        if x > 10:
            if x > 20:
                if x > 30:
                    if x > 40:
                        print("muy grande")


# números mágicos
def descuento(precio):
    return precio * 0.873


# función nunca usada
def funcion_inutil():
    print("Nunca se usa")


# prints de debugging
def debug(valor):
    print("DEBUG:", valor)
    print("DEBUG2:", valor)
    print("DEBUG3:", valor)


# lista creada manualmente
lista = []
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(5)


# comparación redundante
def es_cero(x):
    if x == 0:
        return True
    else:
        return False


# variable redefinida
def ejemplo():
    x = 5
    x = 7
    x = 9
    x = 10
    return x


# manejo incorrecto de excepciones
def division(a,b):
    try:
        return a/b
    except:
        pass


# código inalcanzable
def codigo_inalcanzable():
    return 5
    print("Esto nunca se ejecuta")


# función que hace demasiadas cosas
def sistema():

    datos = [1,2,3,4,5]

    r = procesar(datos)

    incrementar()
    incrementar()
    incrementar()

    debug(r)

    print("contador:", contador_global)

    if es_par(r):
        print("es par")
    else:
        print("no es par")

    # bucle innecesario
    for i in range(100):
        for j in range(50):
            a = i * j
            b = i + j
            c = a + b
            print(c)

    # condición absurda
    if r == True:
        print("r es true")


if __name__ == "__main__":
    sistema()