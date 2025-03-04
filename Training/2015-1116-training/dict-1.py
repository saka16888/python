#### Dictionaries #########################################

brands = {
    'raymond': 'mac',
    'rachel': 'pc',
    'matthew': 'vtech',
}

print(type(brands))          # show type
print(len(brands))           # show size
print(brands)                # show contents
print(brands['rachel'])      # key lookup
brands['matthew'] = 'asus'   # store a new key/value pair
print(brands)
del brands['raymond']        # remove a key
print('matthew' in brands)   # membership test
print(brands)

print(brands.keys())
print(brands.values())
print(brands.items())

print("*" * 50)
dog={"color": "black","size":"big"}
cat={"color": "white","size":"small"}

animal=[dog,cat]
def search_key(key,animal):
    for a,v in animal:
        try:
            print(animal[key==a])
            #print(a.keys())
            #print(a.items())
        except KeyError:
            pass
    else:
        raise KeyError()

search_key("black",animal)
