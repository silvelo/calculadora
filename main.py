from operaciones.suma import sumar

def main():
    print("=== Calculadora básica ===")
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    resultado = sumar(num1, num2)
    print(f"Resultado de la suma: {resultado}")

if __name__ == "__main__":
    main()
