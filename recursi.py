def mult(x, y):
    # Caso base: si y es 0, el producto es 0
    if y == 0:
        return 0
    # Si y es negativo, convertimos el problema a positivo para la recursión
    elif y < 0:
        return -mult(x, -y)
    # Llamada recursiva: sumar x a sí mismo y veces
    else:
        return x + mult(x, y - 1)


