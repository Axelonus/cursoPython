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
            


def drawHangman(score):
    rope = []
    ropeNoKnot = [
        chr(9552)+chr(9552)+chr(9552)+chr(9552)+chr(9552)+chr(9552)+chr(9552)+chr(9552)+chr(9559)+"\n",
        "        "+chr(9122)+"\n",
        "        "+chr(9122)+"\n"
    ]
    head = []
    lilWorriedHead = []
    worriedHead = []
    veryWorriedHead = []
    deadHead = []
    torso = []
    torsoLeftArm = []
    torsoBothArm = [
        "        "+chr(9617)+"\n",
        "     "+chr(11516)+chr(9617)+chr(9617)+chr(9617)+chr(9617)+chr(9617)+chr(11513)+"\n",
        "    "+chr(11516)+"  "+chr(9617)+chr(9617)+chr(9617)+"  "+chr(11513)+"\n",
        "   "+chr(11516)+"   "+chr(9617)+chr(9617)+chr(9617)+"   "+chr(11513)+"\n",
        "   "+chr(5208)+"   "+chr(9617)+chr(9617)+chr(9617)+"   "+chr(5207)+"\n"
    ]
    leftPaw = []
    bothPaw = []
    if score >=6:
        rope = [
            chr(9552)+chr(9552)+chr(9552)+chr(9552)+chr(9552)+chr(9552)+chr(9552)+chr(9552)+chr(9559)+"\n",
            "        "+chr(9122)+"\n",
            "        "+chr(9122)+"\n",
            "       "+chr(9581)+chr(9524)+chr(9582)+"\n",
            "       "+chr(9584)+"-"+chr(9583)+"\n"
        ]
        print("".join(rope))
    elif score == 5:
        head = [
            "      ₩₩₩₩₦ "+"\n",
            "    （＾▽＾）"+"\n"
        ]
        print("".join(ropeNoKnot)+"".join(head))
    elif score == 4:
        lilWorriedHead = [
            "      ₩₩₩₩₦ "+"\n",
            "     (ㆆ_ㆆ)"+"\n"
        ]
        torso = [
            "        "+chr(9617)+"\n",
            "      "+chr(9617)+chr(9617)+chr(9617)+chr(9617)+chr(9617)+"\n",
            "       "+chr(9617)+chr(9617)+chr(9617)+"\n",
            "       "+chr(9617)+chr(9617)+chr(9617)+"\n",
            "       "+chr(9617)+chr(9617)+chr(9617)+"\n"
        ]
        print("".join(ropeNoKnot)+"".join(lilWorriedHead)+"".join(torso))
    elif score == 3:
        worriedHead = [
            "      ₩₩₩₩₦ "+"\n",
            "     (▔﹏▔)"+"\n"
        ]
        torsoLeftArm = [
            "        "+chr(9617)+"\n",
            "     "+chr(11516)+chr(9617)+chr(9617)+chr(9617)+chr(9617)+chr(9617)+"\n",
            "    "+chr(11516)+"  "+chr(9617)+chr(9617)+chr(9617)+"\n",
            "   "+chr(11516)+"   "+chr(9617)+chr(9617)+chr(9617)+"\n",
            "   "+chr(5208)+"   "+chr(9617)+chr(9617)+chr(9617)+"\n"
        ]
        print("".join(ropeNoKnot)+"".join(worriedHead)+"".join(torsoLeftArm))
    elif score == 2:
        worriedHead = [
            "      ₩₩₩₩₦ "+"\n",
            "     (▔﹏▔)"+"\n"
        ]
        print("".join(ropeNoKnot)+"".join(worriedHead)+"".join(torsoBothArm))
    elif score == 1:
        veryWorriedHead = [
            "      ₩₩₩₩₦ "+"\n",
            "     (≧口≦)"+"\n"
        ]
        leftPaw = [
            "       "+chr(11004)+"\n",
            "       "+chr(11004)+"  "+"\n",
            "       "+chr(11004)+"   "+"\n",
            "      "+chr(5709)+"   "+"\n"
        ]
        print("".join(ropeNoKnot)+"".join(veryWorriedHead)+"".join(torsoBothArm)+"".join(leftPaw))
    else:
        deadHead = [
            "      ₩₩₩₩₦ "+"\n",
            "      (X_X)"+"\n"
        ]
        bothPaw = [
            "       "+chr(11004)+" "+chr(11004)+"\n",
            "       "+chr(11004)+" "+chr(11004)+"\n",
            "       "+chr(11004)+" "+chr(11004)+"\n",
            "      "+chr(5709)+"   "+chr(5708)+"\n"
        ]
        print("".join(ropeNoKnot)+"".join(deadHead)+"".join(torsoBothArm)+"".join(bothPaw))




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
    #se crea variable para llevar puntaje
    score = 6


    drawing(wordList)
    drawHangman(score)
    #print(word)
    #userTry = input("    ingresa una letra: ")
    while guessList !=wordList and score > 0:
        userTry = input("    ingresa una letra: ").lower()
        if userTry in wordList:
            # verifyNReturn(wordList,userTry)
            guessList = verifyNReturn(wordList, userTry, guessList)
        else:
            score -= 1
        drawing(wordList,guessList)
        drawHangman(score)
    if score > 0 :
        print("""
            fELICIDADES!!!
            GANASTE
            LA PALABRA ERA: """, word.upper())
    else:
        print("""
            LOOSER
            LA PALABRA ERA: """, word.upper())




    #considerar buscar como quitar acentos a futúro

if __name__ == '__main__':
    run()
