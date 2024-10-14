

#Fibonaci utilizando recursividad
def fibonacci(n):
    if n<=1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

#Fibonaci utilizando recursividad y diccionario
memo = {}
def fibonacciMem(n):
    # Verifica si el resultado ya está en el memo
    if n in memo:
        return memo[n]
    # Casos base
    if n <= 1:
        return 1  # Devuelve 0 para n = 0 y 1 para n = 1
    # Calculamos el número recursivamente y lo almacenamos en memo
    memo[n] = fibonacciMem(n - 1) + fibonacciMem(n - 2)
    return memo[n]


#Pruebas
print(fibonacci(5))
print(fibonacciMem(5))







