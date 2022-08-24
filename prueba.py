def operacionMatematica():
    while True:
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        opc = int(input("Elija una opción:"))
        
        if opc == 1:
            num1 = int(input("Ingrese el primer número: "))
            num2 = int(input("Ingrese el segundo número: "))
            print(f"{num1} + {num2} = {num1 + num2}")
        elif opc == 2:
            num1 = int(input("Ingrese el primer número: "))
            num2 = int(input("Ingrese el segundo número: "))
            print(f"{num1} - {num2} = {num1 - num2}")
        elif opc == 3:
            num1 = int(input("Ingrese el primer número: "))
            num2 = int(input("Ingrese el segundo número: "))
            print(f"{num1} * {num2} = {num1 * num2}")
        elif opc == 4:
            num1 = int(input("Ingrese el primer número: "))
            num2 = int(input("Ingrese el segundo número: "))
            print(f"{num1} / {num2} = {num1 / num2}")
        elif opc == 5:
            print("Saliendo...")
            break
        input("Presione enter para continuar...")