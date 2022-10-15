def mcmu(a,b,c):
    maximo = max(a,b,c)
    mcm = maximo
    while True:
        if mcm % a == 0 and mcm % b == 0  and mcm % c == 0:
            return mcm
        mcm+=maximo

def run():
    sqrd_nats = []

    # #Imprime cuadrados de los primeros 100 números naturales.    
    # for i in range(1,101):
    #     sqrd_nats.append(i*i)
    # print(sqrd_nats)

    # #imprime el cuadrado de los números que no son divisibles entre 3
    # for i in range(1,101):
    #     if i**2 %3 != 0:
    #         sqrd_nats.append(i*i)
    # print(sqrd_nats)
    # print(len(sqrd_nats))

    #imprime el cuadrado de los números que no son divisibles entre 3 con list comprehensions 
    # [element for element in iterable if condition]
    sqrs = [i**2 for i in range(1,101) if i % 3 != 0]
    print(sqrs)

    
    mcm = mcmu(4,6,9)
    print(mcm)
    homework = [i for i in range(1,100000) if i % mcm == 0]
    print(homework)


if __name__ == '__main__':
    run()