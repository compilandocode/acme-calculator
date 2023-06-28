def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División entre cero no está definida"
def porcentaje(a, b):
    return (a * b) / 100
def potencia(a, b):
    return a ** b
# Mostrar opciones disponibles
print("Opciones de operaciones:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Porcentaje")
print("6. Potencia")

# Solicitar opción al usuario
opcion = int(input("Selecciona una opción (1-6): "))

# Verificar opción seleccionada y realizar la operación correspondiente
if opcion >= 1 and opcion <= 6:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == 1:
        resultado = suma(num1, num2)
    elif opcion == 2:
        resultado = resta(num1, num2)
    elif opcion == 3:
        resultado = multiplicacion(num1, num2)
    elif opcion == 4:
        resultado = division(num1, num2)
    elif opcion == 5:
        resultado = porcentaje(num1, num2)
    elif opcion == 6:
        resultado = potencia(num1, num2)

    print("Resultado:", resultado)
else:
    print("Opción inválida. Por favor, selecciona una opción válida.")
