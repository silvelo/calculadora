from operaciones.resta import restar
from operaciones.suma import suma


def main():
    print("=== Calculadora básica ===")
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    resultado = suma(num1, num2)
    print(f"Resultado de la suma: {resultado}")

    resultado_resta = restar(num1, num2)
    print(f"Resultado de la resta: {resultado_resta}")


if __name__ == "__main__":
    main()
