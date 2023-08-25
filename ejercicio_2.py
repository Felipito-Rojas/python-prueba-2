def main():
    print("""convertidor de cantidades
          (1)kilometros a millas
          (2)millas a kilometros
          (3)kilogramos a libras
          (4)libras a kilogramos
          (5)fahrenheit a celsius
          (6)celsius a fahrenheit
          (7)salir""")
    opcion=int(input("Seleccione una opcion: "))
    while (opcion > 0) and (opcion < 6):
        if opcion == 1:
            kilometros=float(input("ingrese una cantidad: "))
            millas=round((kilometros*0.621371),4)
            print(f"La convercion de {kilometros}Km es equivalente a {millas} millas")
        elif opcion == 2:
            millas=float(input("ingrese una cantidad: "))
            kilometros=round((millas*1.60934),4)
            print(f"La convercion de {millas} millas es equivalente a {kilometros}km")
        elif opcion == 3:
            kilogramos=float(input("ingrese una cantidad: "))
            libras=round((kilogramos*2.20462),4)
            print(f"la conversion de {kilogramos}kg a libras es de {libras}lb")
        elif opcion == 4:
            libras=float(input("ingrese una cantidad: "))
            kilogramos=round((libras*0.453592),4)
        elif opcion == 5:
            celsius=float(input("ingrese una cantidad: "))
            fahrenheit=round(((celsius*(9/5))+35),4)
            print(f"la convercion de {fahrenheit}f es equivalente a {celsius}c")
        else:
            fahrenheit=float(input("ingrese una cantidad: "))
            celsius=round(((fahrenheit-32)*(5/9)),4)
            print(f"la conversion de {celsius}c es equivalente a {fahrenheit}f")
        opcion=int(input("Seleccione una opcion: "))
    print("Que tenga buen dia")

        
if __name__=="__main__":
    main()