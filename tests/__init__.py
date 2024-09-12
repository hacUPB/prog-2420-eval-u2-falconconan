def saludo( ):
    ls_genero=["sr","sra"]
    control=True
    while control==True:
        genero=input("ingrese sr. o sra.") 
        if genero in ls_genero:
            nombre=input("cual es su nombre")
            apellido=input("cual es su apellido")
            control=False
            return  genero, nombre, apellido
        else:
            print("dato no valido")
            control=True

        
genero,nombre,apellido=saludo()
print (genero,nombre,apellido," ¡Bienvenido a FastFast Airlines!")
#-----------------------------------------------------------------------------
#seleccion de vuelo
def seleccion_de_vuelo():
    ls_ciudades = ["medellin", "bogota", "cartagena"]
    ls_sem_lab = ["lunes", "martes", "miercoles", "jueves"]
    ls_fin_sem = ["viernes", "sabado", "domingo"]
    
    origen_deseado = input(f"A dónde te diriges entre {ls_ciudades} ")
    destino_deseado = input(f"Hacia dónde te diriges entre {ls_ciudades} ")
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

origen, destino, dia, precios = seleccion_de_vuelo()
if precios:
    print(f"El precio del vuelo es: {precios}")


#-----------------------------------------------------------------------------
#seleccion de asiento

