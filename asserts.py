def divisors(num):
    divs=[]
    for i in range(1,num+1):
        if num % i ==0:
            divs.append(i)
    return divs


def run():
    try:
        num = input("ingresa un número ╰(*°▽°*)╯: ")
        numint = int(num)
        assert numint >0, "solo se pueden escribir números mayores a 0 (╯▔皿▔)╯"
        divs = divisors(numint)
        print(divs)
        print("mi trabajo aquí ha terminado (✿◡‿◡)")
    except ValueError:
        print("solo se pueden escribir números (╯▔皿▔)╯")



if __name__ == '__main__':
    run()