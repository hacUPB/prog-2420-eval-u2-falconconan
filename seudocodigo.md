# problema 1

```
inicio
    leer nombre 
    leer apellido
    definir x=sr.
    definir y=sra.
    imrpimir ("si usd. es hombre digite [x] si no digite [y]" )
    leer genero
    si genero = x 
        print (x,nombre,apellido," ¡Bienvenido a FastFast Airlines!)
    si no 
        print (y,nombre,apellido," ¡Bienvenido a FastFast Airlines!)
    
    //seleccion de vuelo

    definir origen=medellin, bogota, catagena
    definir destino=medellin, bogota, catagena
    definir semana_lab=lunes, martes, miercoles, jueves
    definir fin_semana
    leer origen_deseado entre origen
    leer destino_deseado entre destino
    leer dia_semana
    leer dia_mes
    si origen_deseado=destino_deseado
        print "pa q puts viaja guvon"
    si no
        si origen_deseado=medellin,destino_deseado=bogota o origen_deseado=bogota, destino_deseado=medellin
            distancia=240
        si origen_deseado=medellin,destino_deseado=cartagena o origen_deseado=cartagena, destino_deseado=medellin
            distancia=461
        si origen_deseado=cartagena,destino_deseado=bogota o origen_deseado=bogota, destino_deseado=cartagena
            distancia=657
        si distancia > 400
            si dia_semana
