import random
import os

#devuelve el comando a emplear para limpiar la pantalla dependiendo del sistema operativo
def osClear():
    if os.uname().sysname =="Linux":
        return "clear"
    else:
        return "cls"

#lee el documento de palabras y elige una al azar
def read():
    words = []
    with open("./archivos/data.txt","r",encoding="utf-8") as f:
        for v in f:
            words.append(v)
        rn = random.randint(0,len(words)-1)
        word = words[rn]
        return word

#Dibuja las lineas a adivinar y las letras adivinadas
def drawing(wordList,rightGuessList = ["DEFAULT"]):
    clearCmd = osClear()
    os.system(clearCmd)
    print("""
    
        Juguemos al ahorcado
    
    """)
    #en caso de que no se introduzca una guesslist se crea una vacía y se dibuja en pantalla
    if rightGuessList[0] == "DEFAULT":
        displayList = list(map(lambda i:i.replace(i," _ "),wordList))
        print("\n"," ".join(displayList),"\n")
    else:
        print("\n"," ".join(rightGuessList),"\n")

#verifica que la palabra sea agregada a la lista guesslist
def verifyNReturn(wordlist,userTry,guessList):
    for i,val in enumerate(wordlist):
        if val == userTry and guessList[i] != userTry:
            guessList[i]=userTry
    return guessList
            


def run():
    #se limpia la pantalla dependiendo del sistema operativo
    clearCmd = osClear()
    os.system(clearCmd)
    #se lee la lista, se elige una palabra random de ella
    word = read()
    #se crea una lista con la palabra elegida eliminando los saltos de linea
    wordList = list(word)
    wordList = [i for i in wordList if i != "\n"]
    #se crea la guesslist con guiones bajos puesto que es la palabra a adivinar aún vacía
    guessList = [" _ " for i in wordList]


    drawing(wordList)
    #print(word)
    #userTry = input("    ingresa una letra: ")
    while guessList !=wordList:
        userTry = input("    ingresa una letra: ").lower()
        if userTry in wordList:
            # verifyNReturn(wordList,userTry)
            guessList = verifyNReturn(wordList, userTry, guessList)
        else:
            continue
        drawing(wordList,guessList)
        

    print("""
       fELICIDADES!!!
       GANASTE
       LA PALABRA ERA: """, word.upper())




    #considerar buscar como quitar acentos a futúro

if __name__ == '__main__':
    run()
