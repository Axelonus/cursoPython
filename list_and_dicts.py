from itertools import count


def run():
    my_list = [1,"Hello",True,4.5]
    my_dict = {"firstname":"Axel","lastname":"Chavez"}
    super_list = [
        {"firstname":"Axel","lastname":"Chavez"},
        {"firstname":"Sergio","lastname":"Figueroa"},
        {"firstname":"Emmanuel","lastname":"Peña"},
        {"firstname":"Aaron","lastname":"Sanchez"},
        {"firstname":"Said","lastname":"Hernandez"}
    ]
    super_dict = {
        "natural_nums":[1, 2, 3,4, 5],
        "integer_num":[-1, -2, 0, 1,2],
        "floating_nums":[1.1, 4.2, 6.43]
    }
    sqrd_nats = []

#imprime listas que están dentro del diccionario super dict
    for k,v in super_dict.items():
        print(k,"-",v)

#imprime valores de los diccionarios que están dentro de lista super list    
    for i in super_list:
        print(i["firstname"],i["lastname"])

#Imprime cuadrados de los primeros 100 números naturales.    
    # for i in range(1,101):
    #     sqrd_nats.append(i*i)
    # print(sqrd_nats)

#imprime el cuadrado de los números que no son divisibles entre 3
    for i in range(1,101):
        if i**2 %3 != 0:
            sqrd_nats.append(i*i)
    print(sqrd_nats)
    print(len(sqrd_nats))
if __name__ == '__main__':
    run()