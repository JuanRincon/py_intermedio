def run():


    my_dict = {i: i**3 for i in range(1,101) if i % 3 != 0} 
    
    print(my_dict)


if __name__ == '__main__':
    run()

""" la forma en que se haría con una función normal de python sería:

def run():
    my_dict ={}


    for i in range(1,101):
        my_dict[i] = i**3

    print(my_dict)


if __name__ == '__main__':
    run()

"""
