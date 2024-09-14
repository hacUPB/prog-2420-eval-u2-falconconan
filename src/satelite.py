
def main():
    altura_inicial=float(input("determine la altura inicial del satelite: "))
    coeficiente_arrastre=float(input("cual es el cooeficiente de arastre con el que se movera la aeronave: "))
    altura_minima=float(input("determine la altura minima de seguridad"))
    altitud_orbita=altura_inicial
    orbitas=0
    for altitud_orbita in range (int(altura_minima)):
        altitud_desendida=altura_inicial*coeficiente_arrastre
        altitud_orbita=-altitud_desendida
        coeficiente_arrastre=coeficiente_arrastre+1e-5
        orbitas+=1
        print(f"para la orbita {orbitas} se descendieron {altitud_desendida}km, su alt final es {altitud_orbita} y su nuevo coef de arraste es{coeficiente_arrastre}")
    print ("simulacion finalizada")


if __name__ == "__main__":
    main()
