# Lista comprehension que duplica los números del 1 al 5
a = [ i**2 for i in range(1,6)]
print(a)

# Función que duplica los números del 1 al 5

def power():
    a = list() 
    for i in range(1,6):
        a.append(i**2)
    print(a)

if __name__ == '__main__':
    power()


# Función regresa la multiplicación de los valores de una lista

my_list = [2, 2, 2, 2, 2]

all_multiplied = 1

for i in my_list:
    all_multiplied *= i

print(all_multiplied)


# Uso con filter, se crea un función que regresa sólo los números pares

my_list = [1, 4, 5, 6, 13, 19, 21]

odd = list(filter(lambda x: x % 2 != 0, my_list))

print(odd)

# uso con map, se crea una función que saca el cuadrado de los números de la lista

my_list = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x**2, my_list))

print(squares)


# reduce, se crea un función que multiplica todos los números de la lista y genera un único valor 

from functools import reduce

my_list = [2, 2, 2, 2, 2]

all_multiplied = reduce(lambda a, b: a * b, my_list) 

print(all_multiplied)
