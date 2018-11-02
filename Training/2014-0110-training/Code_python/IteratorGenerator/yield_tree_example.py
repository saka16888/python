"""
Provide additional examples of the implementation of generators and iterators.
"""


class Node:
    def __init__(self, data, children=None):
        self.initlevel = 0
        self.data = data
        if children is None:
            self.children = []
        else:
            self.children = children

    def set_initlevel(self, initlevel):
        self.initlevel = initlevel

    def get_initlevel(self):
        return self.initlevel

    def addchild(self, child):

        self.children.append(child)

    def get_data(self):
        return self.data

    def get_children(self):
        return self.children

    def show_tree(self, level):
        self.show_level(level)
        print 'data: %s' % (self.data, )
        for child in self.children:
            child.show_tree(level + 1)

    def show_level(self, level):
        print '   ' * level,

    #
    # Generator method #1
    # This generator turns instances of this class into iterable objects.
    #
    def walk_tree(self, level):
        yield (level, self, )
        for child in self.get_children():
            for level1, tree1 in child.walk_tree(level+1):
                yield level1, tree1

    def __iter__(self):
        return self.walk_tree(self.initlevel)


#
# Generator method #2
# This generator uses a support function (walk_list) which calls
#   this function to recursively walk the tree.
# If effect, this iterates over the support function, which
#   iterates over this function.
#
def walk_tree(tree, level):
    yield (level, tree)
    for child in walk_list(tree.get_children(), level+1):
        yield child


def walk_list(trees, level):
    for tree in trees:
        for tree in walk_tree(tree, level):
            yield tree


#
# Generator method #3
# This generator is like method #2, but calls itself (as an iterator),
#   rather than calling a support function.
#
def walk_tree_recur(tree, level):
    yield (level, tree,)
    for child in tree.get_children():
        for level1, tree1 in walk_tree_recur(child, level+1):
            yield (level1, tree1, )


def show_level(level):
    print '   ' * level,


def test():
    a7 = Node('777')
    a6 = Node('666')
    a5 = Node('555')
    a4 = Node('444')
    a3 = Node('333', [a4, a5])
    a2 = Node('222', [a6, a7])
    a1 = Node('111', [a2, a3])
    initLevel = 2
    a1.show_tree(initLevel)
    print '=' * 40
    for level, item in walk_tree(a1, initLevel):
        show_level(level)
        print 'item:', item.get_data()
    print '=' * 40
    for level, item in walk_tree_recur(a1, initLevel):
        show_level(level)
        print 'item:', item.get_data()
    print '=' * 40
    a1.set_initlevel(initLevel)
    for level, item in a1:
        show_level(level)
        print 'item:', item.get_data()
    iter1 = iter(a1)
    print iter1
    print iter1.next()
    print iter1.next()
    print iter1.next()
    print iter1.next()
    print iter1.next()
    print iter1.next()
    print iter1.next()
##    print iter1.next()
    return a1

if __name__ == '__main__':
    test()
