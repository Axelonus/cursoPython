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
    pyworkers = list(filter(lambda wk : wk["language"]=="python", DATA))
    pyworkers = list(map(lambda wk : wk["name"],pyworkers))
    for wk in pyworkers:
        print(wk)

    #Obteniendo todos los trabajadores de Platzi
    print(
        """
        Trabajadores de Platzi
        """
    )
    plaworkers = list(filter(lambda wk : wk["organization"] == "Platzi", DATA))
    plaworkers = list(map(lambda wk : wk["name"], plaworkers))
    for wk in plaworkers:
        print(wk)

        #Obteniendo todos los trabajadores de edad +18
    print(
        """
        Adultos
        """
    )
    legals = [wk["name"] for wk in DATA if wk["age"]>18]
    for wk in legals:
        print(wk)

    #Obteniendo todos los trabajadores con una nueva key llamada old con valor booleano indicando si son mayores a 70 años
    print(
        """
        ¿son mayores a 70?
        """
    )
    olds = [{**wk,**{"old":wk["age"]>70}} for wk in DATA]
    for wk in olds:
        print(wk)

    # olds = [{**wk,**{"old":wk["age"]}} for wk in DATA if wk["age"]>70]
    # for wk in olds:
    #     print(wk)


if __name__ == '__main__':
    run()