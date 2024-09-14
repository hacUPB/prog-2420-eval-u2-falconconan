from __init__ import saludo,seleccion_de_vuelo
from random import randint

def main():
    control=True
    while control:
        genero,nombre,apellido=saludo()
        print (genero,nombre,apellido," ¡Bienvenido a FastFast Airlines!")  
        origen, destino, dia, precios = seleccion_de_vuelo()
        fila=randint(1,100)
        asiento=int(input("le gustaria ir en\n 1.ventana \n 2.pasillo \n 3.no tengo problema"))
        if asiento==1:
            print(f"{genero} {nombre} {apellido} usted se va en el asiento A {fila} de {origen} a {destino} el dia {dia}\n su total a pagar es: {precios}")
        elif asiento==2:
            print(f"{genero} {nombre} {apellido} usted se va en el asiento B {fila} de {origen} a {destino} el dia {dia}\n su total a pagar es: {precios}")
        elif asiento==3:
            print(f"{genero} {nombre} {apellido} usted se va en el asiento C {fila} de {origen} a {destino} el dia {dia}\n su total a pagar es: {precios}")
        else:
            print("dato no valido")    
        print ("TODOS LOS DATOS SON CORRECTOS\n 1.si \n 2.no")
        opcion=int(input("ingrese opcion"))
        if opcion==1:
            control=False
            print("vuelo elegido")
        else:
            print("opcion no valida")
            


if __name__ == "__main__":
    main()
