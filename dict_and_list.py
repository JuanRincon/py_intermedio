def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "facundo", "lastname": "García"}

    super_list = [
        {"firstname": "Facudno", "lastname": "García"},
        {"firstname": "Miguel", "lastname": "Torres"},
        {"firstname": "Pepe", "lastname": "Rodelo"},
        {"firstname": "Susana", "lastname": "Martinez"},
        {"firstname": "José", "lastname": "García"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key in range(len(super_list)):
        print(super_list[key])


if __name__ == '__main__':
    run()
