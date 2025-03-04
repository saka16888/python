def sockPair(ar):
    '''

    For example, there are  n=7 socks with colors ar=[1,2,1,2,1,3,2].
    There is one pair of color 1 and one of color 2.
    There are three odd socks left, one of each color. The number of pairs is 2.
    :param ar:
    :return:
    '''

    color={}
    for i in ar:
        print("i",i)
        if i in color:
            color[i] += 1
        else:
            color[i] = 1

    #print(color)
    pair=0
    for c in color:
        pair += color[c] //2
    return pair

ar=[1,2,1,2,1,3,2]
print(sockPair(ar))

ar=[]
print(sockPair(ar))

color={
    1 : 3 ,
    2 : 4 ,
}

for i in color:
    print(i,color[i])


# color[3] += 1 , Error no init value for color[3]
