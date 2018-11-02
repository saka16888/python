# Use cases:
#     Variable lookups:     ChainMap([locals(), globals(), __builtins__.__dict__])
#     Attribute lookups:    ChainMap([inst.__dict__, cls.__dict__, base_cls.__dict__])
#     Bash lookups:         ChainMap(os.environ['PATH'].split(':'))
#     Settings:             ChainMap([command_line_args, os.environ, application_default])
#     Parameters in PyATS:  ChainMap([easypy commandline, main(kwargs), class_and_method_defaults])

class ChainMap:
    'Tool for combining a list of dictionaries to create a single dictionary view'

    def __init__(self, mappings):
        self.mappings = mappings
        print(self.mappings)

    def __getitem__(self, key):
        for mapping in self.mappings:
            try:
                print(mapping)
                return mapping[key]
            except KeyError:
                pass
        raise KeyError(key)

if __name__ == '__main__':

    momma = {'kale': 'Yuck!', 'vegetables': 'Tasty!'}
    daddy = {'candybar': 'Treat', 'steak': 'Healthy', 'vegetables': 'Very Tasty!'}
    granny = {'cookie': 'chocolate chip'}

    adults = ChainMap([momma, daddy, granny])
    print(adults['cookie'])
    print(adults['steak'])
#    print(adults['razor blades'])
