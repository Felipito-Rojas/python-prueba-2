def main():
    num=int(input("ingrese un numero: "))
    if (num%2 == 0) or (num%3 ==0):
        print(f"el numero {num} No es primo")
        return False
    else:
        print(f"el numero {num} es primo")
        return True

if __name__=="__main__":
    main()