

def seleccion_de_vuelo():
    from datetime import datetime
    import calendar
    ls_ciudades = ["medellin", "bogota", "cartagena"]
    origen_deseado = input(f"A dónde te diriges entre {ls_ciudades} ")
    destino_deseado = input(f"Hacia dónde te diriges entre {ls_ciudades} ")
    if origen_deseado == destino_deseado:
        print("No debes viajar")
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
    
    year=int(input("en que año desea viajar: "))
    print(calendar.calendar(year))
    fecha_viaje=input("introdusca la fecha de su viaje en formato DD/MM/AAAA: ")
    fecha_seleccionada=datetime.strptime(fecha_viaje,"%d/%m/%Y")
    hoy=datetime.now()
    control=True
    while control==True:
        if fecha_seleccionada>hoy:
            if fecha_seleccionada.weekday() in [0,1,2,3] and distancia<400 :
                precio = 79900
            else:
                precio = 156900        
            if fecha_seleccionada.weekday() in [4,5,6]and distancia<400:
                precio = 119900
            else:
                precio = 213000   
            control=False
            return origen_deseado, destino_deseado, fecha_seleccionada, precio
        else:
            print("dato no valido")
            control=True

origen, destino, dia, precios = seleccion_de_vuelo()
print(f"El precio del vuelo es: {precios}\n el dia: {dia}")