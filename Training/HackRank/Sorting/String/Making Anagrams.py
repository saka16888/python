def number_needed(a, b):
    # s1 = sorted ([i for i in a])
    # s2 = sorted ([i for i in b])
    s1 = [i for i in a]
    s2 = [i for i in b]
    if len (s1) < len (s2):
        t1 = s1
        t2 = s2
    else:
        t1 = s2
        t2 = s1
    tmp=t1.copy()
    for i in tmp:
        if i in t2:
            t1.remove(i)
            t2.remove(i)
    print (t1, "\n", t2)
    return (len (t1 + t2))


a = "abdsbf"
b = "abbdq"
print ("a=",a,"\nb=",b)
print (number_needed (a, b))

a = "cde"
b = "abc"
print (number_needed (a, b))

a = "fcrxzwscanmligyxyvym"
b = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"
print (number_needed (a, b))
