
dog={"color": "black","size":"big"}
cat={"color": "white","size":"small"}

animal=[dog,cat]
def search_key(key,animal):
    for a,v in animal:
        try:
            print(a)
            #print(a.keys())
            #print(a.items())
        except KeyError:
            pass
    else:
        raise KeyError()

search_key("color",animal)
