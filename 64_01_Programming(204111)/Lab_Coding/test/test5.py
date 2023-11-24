# test 5

import string
def main():
    print(decode("aceiklmr-",'''\
3
5 3 4 2
3 1 2 8 1 7 2 0 86\
'''))

def decode(code_table, text):
    t = text.split("\n")
    # t = ['3', '5 3 4 2', '3 1 2 8 1 7 2 0 86']
    item = []
    for i in t:
        i = i.split(" ")
        item.append(i)
    # item = [['3'], ['5', '3', '4', '2'], ['3', '1', '2', '8', '1', '7', '2', '0', '86']]
    res = []
    for i in item:
        m = []
        for j in i:
            if j == "":
                m.append(j)
            elif j == " ":
                m.append(j)
            elif str(abs(int(j))).isdigit() == True:
                r = int(j)
                if r >= 0 and r < len(code_table):
                    r = code_table[r]
                else:
                    r = "_"
                m.append(r)
        res.append(m)
    # res = [['i'], ['l', 'i', 'k', 'e'], ['i', 'c', 'e', '-', 'c', 'r', 'e', 'a', '_']]
    res2 = []
    for i in range(len(res)):
        if len(res[i]) == 0:
            m = ""
        else:
            for j in range(len(res[i])):
                m = ",".join(res[i])
        res2.append(m)
    # res2 = ['i', 'l,i,k,e', 'i,c,e,-,c,r,e,a,_']
    for i in range(len(res2)):
        for j in ",":
            res2[i] = res2[i].replace(j, "")
    # res2 = ['i', 'like', 'ice-crea_']
    res3 = "\n".join(res2)
    print(res3)

if __name__ == '__main__':
    main()