def divisors(num):
    try:
        if num <=0:
            raise ValueError("Solo se pueden introducir números mayores a 0")
        else:
            divs=[]
            for i in range(1,num+1):
                if num % i ==0:
                    divs.append(i)
            return divs
    except ValueError as ve:
        return ve


def run():
    try:
        num = int(input("ingresa un número ╰(*°▽°*)╯: "))
        divs = divisors(num)
        print(divs)
        if type(divs)!=ValueError:
            print("mi trabajo aquí ha terminado (✿◡‿◡)")
    except ValueError:
        print("solo se pueden escribir números enteros (╯▔皿▔)╯")


if __name__ == '__main__':
    run()