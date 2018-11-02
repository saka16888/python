# simple_node.py

Indents = ['    ' * n for n in range(10)]

class Node(object):
    def __init__(self, name=None, children=None):
        self.name = name
        if children is None:
            self.children = []
        else:
            self.children = children
    def show_name(self, indent):
        print('%sname: %s' % (Indents[indent], self.name))
    def show(self, indent=0):
        self.show_name(indent)
        indent += 1
        for child in self.children:
            child.show(indent)

def test1():
    n1 = Node('N1')
    n2 = Node('N2')
    n3 = Node('N3')
    n4 = Node('N4')
    n5 = Node('N5', [n1, n2,])
    n6 = Node('N6', [n3, n4,])
    n7 = Node('N7', [n5, n6,])
    n7.show()

class Plant(Node):
    def __init__(self, name, height=-1, children=None):
        Node.__init__(self, name, children)
        self.height = height
    def show(self, indent=0):
        self.show_name(indent)
        print('%sheight: %s' % (Indents[indent], self.height))
        indent += 1
        for child in self.children:
            child.show(indent)

class Animal(Node):
    def __init__(self, name, color='no color', children=None):
        Node.__init__(self, name, children)
        self.color = color
    def show(self, indent=0):
        self.show_name(indent)
        print('%scolor: "%s"' % (Indents[indent], self.color))
        indent += 1
        for child in self.children:
            child.show(indent)

def test2():
    n1 = Animal('scrubjay', 'gray blue')
    n2 = Animal('raven', 'black')
    n3 = Animal('american kestrel', 'brown')
    n4 = Animal('red-shouldered hawk', 'brown and gray')
    n5 = Animal('corvid', 'none', [n1, n2,])
    n6 = Animal('raptor', children=[n3, n4,])
    n7a = Animal('bird', children=[n5, n6,])
    n1 = Plant('valley oak', 50)
    n2 = Plant('canyon live oak', 40)
    n3 = Plant('jeffery pine', 120)
    n4 = Plant('ponderosa pine', 140)
    n5 = Plant('oak', children=[n1, n2,])
    n6 = Plant('conifer', children=[n3, n4,])
    n7b = Plant('tree', children=[n5, n6,])
    n8 = Node('birds and trees', [n7a, n7b,])
    n8.show()


if __name__ == '__main__':
    test1()
    test2()