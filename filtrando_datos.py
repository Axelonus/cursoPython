DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]



def run():
    #Obteniendo los programadores de python
    print(
        """
        Programadores de Python
        """
    )
    propy = [worker["name"] for worker in DATA if worker["language"]== "python"]
    for worker in propy:
        print(worker)
    #Obteniendo todos los trabajadores de Platzi
    print(
        """
        Trabajadores de Platzi
        """
    )
    platzi = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    for worker in platzi:
        print(worker)
    #Obteniendo todos los trabajadores de edad +18
    print(
        """
        Adultos
        """
    )
    adultos = list(filter(lambda worker: worker["age"]>18, DATA))
    adultos = list(map(lambda worker: worker["name"], adultos))
    for worker in adultos:
        print(worker)
    #Obteniendo todos los trabajadores con una nueva key llamada old con valor booleano indicando si son mayores a 70 años
    print(
        """
        ¿son mayores a 70?
        """
    )
    older = list(map(lambda worker:{**worker,**{"old":worker["age"]>70}},DATA))
    for worker in older:
        print(worker)


if __name__ == '__main__':
    run()