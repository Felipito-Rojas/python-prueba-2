def main():
    frase=input("ingrese una frase: ")
    palindromo=frase.lower()
    print(palindromo)
    palindromo=frase.replace(" ","")
    print(palindromo)
    if palindromo == palindromo[::-1]:
        print(f"La palabra {frase} es un palindromo")
    else:
        print(f"La palabra {frase} NO es un palindromo")
    
if __name__ == "__main__":
    main()