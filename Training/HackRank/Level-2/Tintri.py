
def addStrSpace(tmp):
    str2=""
    for i in range(len(tmp)):
        str2 += tmp[i]
        print('id(str2) =',id(str2),str2)
        if i % 3 == 2 :
            str2 += " "
    str2.rstrip()
    return (str2)

tmp="asdfjlasdjflsdakfjsda"
print(addStrSpace(tmp))

tmp="asd"
print(addStrSpace(tmp),"end")

