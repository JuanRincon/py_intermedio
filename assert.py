
""" En este script se calculan los números por los que es divisible
un número ingresado, y se maneja excepciones en caso que el usuario
no ingrese un número (una letra), o ingrese un número negativo
"""

# un assert es una función de condición que en caso de no cumplirse
# una condición específica lanza un mensaje de error en la ejecución del programa
# indicando lo que se debe hacer

def divisors(num):
    divisors = list()
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    num = input("Ingresa un número: ")
    assert int(num)>0, "Debes ingresar un valor positivo"
    #assert num.isnumeric(), "Debes ingresar un número" 
    print(divisors(int(num)))
    print('Terminó mi programa')   


if __name__ == '__main__':
    run()
