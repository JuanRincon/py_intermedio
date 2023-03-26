
def run():
    squares = []
    for i in range(100):
        squares.append(pow(i + 1, 2))
    
        a = squares[i]
        if a % 3 != 0:
            print(squares[i])

if __name__ == '__main__':
    run()

""" La solución propuesta por el profesor
aparece acá abajo (La principal diferencia es que en el mio los incluyo pero no los imprimo,
                    mientras que en la del profesor no se incluye en la lista y se imprime)


def run():
    squares = []
    for i in range(1, 101):
        if i % 3 != 0:
            squares.append(i**2)

    print(squares)

if __name__ == '__main__':
    run()
"""
