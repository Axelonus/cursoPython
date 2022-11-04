def verifyPalindromes(string):
    words = []
    length = len(string)
    print(length)
    assert length < 5000 , "too much words for me :("
    #count = length
    while len(string) > 3:
        string_in = string
        string_in_rev = string_in[::-1]
        while len(string_in_rev) > 3:
            if string_in == string_in_rev:
                words.append(string_in)
            string_in_rev = string_in_rev[1:]
            string_in = string_in_rev[::-1]
        string = string[1:]
    insert(words)


def run():
    data = ""
    with open('./files/lecture.txt','r',encoding='utf-8') as f:
        data = f.read()
    my_data = "".join(i for i in data if i.isalnum()).lower()
    #re.sub('[^A-Za-z0-9]+', '', data)
    verifyPalindromes(my_data)

def insert(my_list):
    my_list = list(set(my_list))
    my_new_list = []
    for i in my_list:
        flag = True
        for j in my_list:
            if len(i) == len(j):
                continue
            if  i in j:
                flag = False
                break
        if flag == True:
            my_new_list.append(i)
    #pals = [i for i in my_list if]
    with open("./files/palindromes.txt", "w", encoding="utf-8") as p:
        for i in my_new_list:
            p.write(i)
            p.write("\n")

if __name__ == '__main__':
    run()