

def lista_de_5_digitos():
    a = [mult4_6_9 for mult4_6_9 in range(1, 100000) if ((mult4_6_9 % 4 == 0) & (mult4_6_9 % 6 == 0) & (mult4_6_9 % 9 == 0))]
    print(a)


if __name__ == '__main__':
    lista_de_5_digitos()
