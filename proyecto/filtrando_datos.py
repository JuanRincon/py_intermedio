from datos_filtrado import DATA

def run():
    # List comprehension  - Arroja el nombre de la lista de unicamente los que programan en python
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    # High order function - Arroja el nombre de la lista de unicamente los que programan en python
    all_python_devs_HOF = list(filter(lambda worker : worker["language"] == "python", DATA))
    all_python_devs_HOF = list(map(lambda worker : worker["name"], all_python_devs_HOF))

    # List comprehension - Trae el nombre de los trabajadores que trabajan en Platzi
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    # High order function - Trae el nombre de los trabajadores que trabajan en Platzi
    all_platzi_workers_HOF = list(filter(lambda worker : worker["organization"] == "Platzi", DATA))
    all_platzi_workers_HOF = list(map(lambda worker : worker["name"] ,all_platzi_workers_HOF))
    

    # List comprehension - Trae el nombre de los trabajadores mayores de 18 años
    all_platzi_adultos = [worker["name"] for worker in DATA if worker["age"] > 18]
    # High order function - Trae el nombre de los trabajadores mayores de 18 años
    all_platzi_adults_HOF = list(filter(lambda worker : worker["age"] > 18, DATA))
    all_platzi_adults_HOF = list(map(lambda worker : worker["name"], all_platzi_adults_HOF)) 


    # High order function
    adults = list(filter(lambda worker : worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    # List comprehension
    adults_LC = [worker["name"] for worker in DATA if worker["age"] > 18]


    # High order function
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    # List comprehension
    old_people_LC = [worker | {"old":worker["age"] > 70} for worker in DATA] 


    for worker in old_people_LC:
        print(worker)


if __name__ == '__main__':
    run()

