import time

def factorial (n):
    respuesta = 1

    while n > 1:
        respuesta*= n
        n-= 1

    return respuesta

def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

if __name__ == '__main__':
    # Definir valores para realizar la prueba de tiempo
    tests = [1000, 10000, 50000, 100000, 200000]

    print(f'Toma de tiempos entre dos algoritmos de factorial.')
    for n in tests:

        comienzo = time.time()
        factorial(n)
        final = time.time()
        time1 = final - comienzo

        comienzo = time.time()
        factorial_r(n)
        final = time.time()
        time2 = final - comienzo

        print(f'    Factorial de {n}:')
        print(f'        Algoritmo 1: {time1}')
        print(f'        Algoritmo 2: {time2}')



