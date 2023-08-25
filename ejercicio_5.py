def main():
    palabra=input("Ingrese una palabra: ")
    letra=input(f"Que letra dese buscar en {palabra} ? :")
    cont=0
    for i in palabra[::1]:
        if letra == i:
            cont+=1
    print(f"la letra {letra} aparece {cont} veces en la palabra {palabra}")

if __name__ == "__main__":
    main()