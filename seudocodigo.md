# problema 1

![diagrama de bloques](image-1.png)

```
inicio
    mientras a=no
        escribir "sr. o sra."
        leer genero 
        escribir "nombre"
        leer nombre 
        escrivir "apellido"
        leer apellido
        print (genero,nombre,apellido," ¡Bienvenido a FastFast Airlines!)
            //seleccion de vuelo

            definir ciudades=medellin, bogota, catagena
            definir semana_lab=lunes, martes, miercoles, jueves
            definir fin_semana=viernes, sabado, domingo
            leer origen_deseado entre ciudades
            leer destino_deseado entre ciudades
            si origen_deseado=destino_deseado
                print "no viajas"
            si no
                leer dia_semana entre semana_lab y fin_semana
                leer dia_mes
                    si origen_deseado=medellin,destino_deseado=bogota o origen_deseado=bogota, destino_deseado=medellin
                        distancia=240
                    si origen_deseado=medellin,destino_deseado=cartagena o origen_deseado=cartagena, destino_deseado=medellin
                        distancia=461
                    si origen_deseado=cartagena,destino_deseado=bogota o origen_deseado=bogota, destino_deseado=cartagena
                        distancia=657
                    si distancia >= 400
                        si dia_semana=semana_lab
                            precio=156900
                        si no
                            precio=213000
                    si no
                        si dia_semana=semana_lab
                            precio=79900
                        si no
                            precio=119900
                    // seleccion de asiento
                    fila=numero random
                    imprimir "asiento de la ventana si o no"
                    leer ventana 
                    si ventana=si
                        imprimir (genero,nombre,apellido,"usted se va en el asiento A",fila,"de",origen_deseado, "a",destino_deseado)
                        imprimir(precio)
                    si no
                        imprimir "asiento del pasillo si o no"
                        leer pasillo
                        si pasillo=si
                            imprimir (genero,nombre,apellido,"usted se va en el asiento B",fila"de",origen_deseado, "a",destino_deseado)
                            imprimir(precio)
                        si no
                            imprimir (genero,nombre,apellido,"usted se va en el asiento C",fila"de",origen_deseado, "a",destino_deseado)
                            imprimir(precio)
    imprimir ("todos los datos con correctos")
    leer a
    para a diferente de si,no
    imprimir("dato no valido, todos los datos con correctos")
    leer a
    fin para
fin
```
# problema 2

![diagrama de bloques](image.png)
## Datos de Entrada
- Altitud inicial: Altitud desde la cual el satélite comienza su órbita (en kilómetros).
- Coeficiente de arrastre: Factor que determina la rapidez con la que el satélite pierde altitud. Este valor aumenta a medida que disminuye la altitud.
- Altitud mínima de seguridad: Altitud por debajo de la cual se considera que el satélite ha reingresado en la atmósfera y se ha desintegrado.

```
inicio
    leer altura_in  
    leer coeficiente_aras   
    leer altura_min        
    definir contador orbita=0
    para alt_inici>alt_min  hasta alt_min>=alt_posorbit
        calcular alt_des= alt_inici*coef_ar
        calcular alt_postorbit=alt_inici-alt_des
        coerf_ar=coef_ar+1e-5
        orbitas=orbitas+1
        imprimir "para la orbita {orbita} se descendieron {alt_des}km, su alt final es {alt_posorbit} y su nuevo coef de arraste es{coef_ar}"
    imprimir "simulacion finalizada"
fin
```

