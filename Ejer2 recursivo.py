def power(x, y):
    # Caso base 1: cualquier número elevado a la potencia 0 es 1
    if y == 0:
        return 1
    # Caso base 2: cualquier número elevado a la potencia 1 es el propio número
    elif y == 1:
        return x
    # Si el exponente es negativo, aplicamos la transformación x^y = 1 / (x^-y)
    elif y < 0:
        return 1 / power(x, -y)
    # Caso recursivo para exponentes positivos
    else:
        return x * power(x, y - 1)

# Programa de prueba
# Prueba con varios ejemplos
test_cases = [
    (2, 3),    # 2^3 = 8
    (5, 0),    # 5^0 = 1
    (7, 1),    # 7^1 = 7
    (3, -2),   # 3^-2 = 1/9
    (-2, 3),   # (-2)^3 = -8
    (4, -1),   # 4^-1 = 0.25
]

for x, y in test_cases:
    resultado = power(x, y)
    print(f"{x}^{y} = {resultado}")