import random
from symbol import decorator
from typing import List, Dict
import operator
from datetime import datetime

def feedback(fun):
    def wrapper():
        start = datetime.now()
        result = fun()
        end = datetime.now()
        timesecs = (end - start).total_seconds()
        if result:
            print(f"Bien hecho, te ha tomado {timesecs} segundos en resolverlo")
        else:
            print("Valla parece que necesitamos practicar un poco más")
    return wrapper

@feedback
def challenge():
    firstnum = random.randint(1,99)
    secondnum = random.randint(1,99)
    randOper = random.randint(1,4)
    operators: Dict[int,] = {1:operator.add, 2:operator.sub, 3:operator.mul, 4:operator.floordiv}
    stringOpers: Dict[str,] = {1:"+", 2:"-", 3:"*", 4:"/"}
    #print(f"cuánto es {firstnum} {stringOpers.get(randOper)}{secondnum}") 
    user = int(input(f"cuánto es {firstnum} {stringOpers.get(randOper)} {secondnum}: "))
    return user == int(operators.get(randOper)(firstnum,secondnum))


def run():
    challenge()

if __name__ == '__main__':
    run()