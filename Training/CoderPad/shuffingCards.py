def shuffingCards(pile1,pile2):

    top=True
    for card in pile1:
        if top:
            pile2.insert(0,card)
            top=False
        else:
            pile2.append(card)
            top=True


first_pile=["ace1","5hearts","3diamonds","4club"]
second_pile=["5A","6H","7D","8C"]

shuffingCards(first_pile, second_pile)
print(second_pile)
