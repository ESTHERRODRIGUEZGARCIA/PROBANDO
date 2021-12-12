#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  calc.py
#  
#  Copyright https://pythones.net
#
############################################-1-##################################################


'''
Explicación del código:
creación de las cuatro funciones básicas de cálculo y también las funciones internas input!

código está dividido en tres partes, esto es intencional para explicar cada parte por separado:

En la primera parte
Creamos cuatro funciones correspondientes al cálculo que habrá disponible (pero aun no las llamamos). 
Habiendo creado las funciones pasamos a la parte dos.

En la segunda parte
Creamos un bucle (que se repite para no dejar continuar al usuario hasta que ingrese los números con
 lo que va a trabajar nuestra calculadora, los cuales se almacenan en variables). El try/except se 
 utiliza para que si surgiera un error no finalizara el programa y nos mostrara un “Error” personalizado 

Una vez que presentamos las entradas también le presentamos al usuario la elección de 4 opciones 
correspondientes al cálculo a realizar el cual se almacena en la variable op.

En la tercera parte
Determinamos el número almacenado en la variable op mediante un If/elif y según sea el número ejecutamos
la llamada a la función correspondiente al cálculo que quiere realizar.

'''
def sumar(): #Definimos la función sumar
    x = a + b
    print (("Resultado"), (x))
def restar():#Definimos la función restar
    x = a - b
    print (("Resultado"), (x))
def multiplicar():#Definimos la función multiplicar
    x = a * b
    print (("Resultado"), (x))
def dividir():#Definimos la función dividir
    x = a / b
    print (("Resultado"), (x))
##########################################-2-###################################################
while True: #Creamos un bucle
    try: #Intentamos obtener los datos de entrada
        a = int(input("Ingresa el primer numero: \n")) #Solicitamos el 1er numero al usuario
        b = int(input("Ingresa el segundo numero: \n"))#Solicitamos el 2do numero al usuario
        print (("Que calculo quieres realizar entre"), (a), ("y"), (b), ("?\n")) #Preguntamos el calc
        op = str(input(""" #Ofrecemos las opciones de cálculo las cuales van a llamar a las funciones
        1- Sumar
        2- Restar
        3- Multiplicar
        4- Dividir \n"""))
##########################################-3-##################################################
        if op == '1':#Si el usuario elige opción 1 llamamos a sumar
            sumar()
            break
        elif op == '2':#Si el usuario elige opción 1 llamamos a restar
            restar()
            break
        elif op == '3':#Si el usuario elige opción 1 llamamos a multiplicar
            multiplicar()
            break
        elif op == '4':#Si el usuario elige opción 1 llamamos a dividir
            dividir()
            break
        else:
            print ("""Has ingresado un numero de opcion erroneo""") #En caso que el numero no se encuentre

    except ZeroDivisionError:
        print ("Nuestro calculador no permite dividir por cero, intenta otro calculo!")

    except:
        print ("Error")
        op = '?'
    finally:
        print ("Gracias por utilizar nuestra calculadora")