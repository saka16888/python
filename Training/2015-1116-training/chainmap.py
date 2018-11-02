momma = {'kale': True, 'vegetables': True}
daddy = {'candybar': True, 'steak': True, 'vegetables': True}
granny = {'cookie': 'chocolate chip'}

key = 'cookie'
adults = [momma, daddy, granny]
print(adults)
for adult in adults:
    try:
        print(adult.keys())
        #break
    except KeyError:
        pass
else:                             # no_break   or   loop_finished_normally
    raise KeyError(key)
