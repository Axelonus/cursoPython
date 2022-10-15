def run():
    #se usan numeros naturales del 1 al 100 como las llaves y los valores se usan los cubos
    mydic = {k:k**3 for k in range(1,101)}
    print(mydic)
    # {key:value for value in iterable if condition}
    #se usan numeros naturales del 1 al 100 como las llaves y los valores se usan los cubos pero se ignoran las llaves que son divisibles entre tres
    mydic2 = {k:k**3 for k in range(1,101) if k % 3 != 0}
    print(mydic2)

    mydic3 = {k:round(k**0.5,2) for k in range(1,1001)}
    print(mydic3)


if __name__ == '__main__':
    run()