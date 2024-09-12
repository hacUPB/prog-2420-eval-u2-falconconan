def saludo( ):
    ls_genero=["sr","sra"]
    control=True
    while control==True:
        genero=input("ingrese sr. o sra.") 
        if genero in ls_genero:
            nombre=input("ingrese su nombre: ")
            apellido=input("ingrese su apellido: ")
            control=False
            return  genero, nombre, apellido
        else:
            print("dato no valido")
            control=True

def seleccion_de_vuelo():
    ls_ciudades = ["medellin", "bogota", "cartagena"]
    ls_sem_lab = ["lunes", "martes", "miercoles", "jueves"]
    ls_fin_sem = ["viernes", "sabado", "domingo"]
    
    origen_deseado = input(f"cual es tu ciudad de partida entre {ls_ciudades} ")
    destino_deseado = input(f"cual es tu ciudad de destino entre {ls_ciudades} ")
    if origen_deseado == destino_deseado:
        print("No debes viajar")
        return
    dia_semana = input("¿Qué día de la semana vas a viajar (lunes, martes, etc.)? ")
    
    if dia_semana not in ls_sem_lab and dia_semana not in ls_fin_sem:
        print("Dato no válido")
        return
    
    if (origen_deseado == "medellin" and destino_deseado == "bogota") or (origen_deseado == "bogota" and destino_deseado == "medellin"):
        distancia = 240
    elif (origen_deseado == "medellin" and destino_deseado == "cartagena") or (origen_deseado == "cartagena" and destino_deseado == "medellin"):
        distancia = 461
    elif (origen_deseado == "bogota" and destino_deseado == "cartagena") or (origen_deseado == "cartagena" and destino_deseado == "bogota"):
        distancia = 657
    else:
        print("Ruta no válida")
        return
    
    if distancia < 400:
        if dia_semana in ls_sem_lab:
            precio = 79900
        else:
            precio = 119900
    else:
        if dia_semana in ls_sem_lab:
            precio = 156900
        else:
            precio = 213000
    
    return origen_deseado, destino_deseado, dia_semana, precio

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
            print(f"{genero} {nombre} {apellido} usted se va en el asiento A {fila} de {origen} a {destino} \n su total a pagar es: {precios}")
        elif asiento==2:
            print(f"{genero} {nombre} {apellido} usted se va en el asiento B {fila} de {origen} a {destino} \n su total a pagar es: {precios}")
        elif asiento==3:
            print(f"{genero} {nombre} {apellido} usted se va en el asiento C {fila} de {origen} a {destino} \n su total a pagar es: {precios}")
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
