""" En este script se calculan los números por los que es divisible
un número ingresado, y se maneja excepciones en caso que el usuario
no ingrese un número (una letra), o ingrese un número negativo
"""


def divisors(num):
    divisors = list()
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:
        num = int(input("Ingresa un número: "))
        if num > 0:
            print(divisors(num))
            print('Terminó mi programa')
        else:
            raise ValueError
    except ValueError:
        print("Debe ingresar un entero positivo")

if __name__ == '__main__':
    run()
