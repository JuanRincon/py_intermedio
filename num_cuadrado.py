
""" def num_al_cuadrado():
    a = list()

    for i in range(100):
        a.append(pow(i + 1, 2))
        print(i, ': ', a[i])


if __name__ == '__main__':
    num_al_cuadrado()
"""
""" La solución propuesta por el profesor
es la siguiente
"""

def run():
    squares = []
    for i in range(1, 101):
        squares.append(i**2)

    print(squares)

if __name__ == '__main__':
    run()
