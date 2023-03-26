""" La funcion lamba de reemplaza la estructura de una función para
resumir todo en una sóla línea como se ve a continuación

"""



a = input('Ingrese la cadena de palabras a verificar si es palindromo: ')
palindrome = lambda palabra:palabra == palabra[::-1]
print('La respuesta a si la cadena es palindromo es:', palindrome(a))





""" La forma en que se haría si fuera una función sería la siguiente

def palindrome(palabra):
    return palabra == palabra[::-1]

a = input('Ingrese la cadena de palabras a verificar si es palindromo: ')

print('La respuesta a si la cadena es palindromo es: ', palindrome(a))

"""
