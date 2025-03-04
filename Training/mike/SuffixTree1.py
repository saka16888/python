class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.suffix_link = None
        self.start = -1
        self.end = -1
        self.suffix_index = -1

class SuffixTree:
    def __init__(self, text):
        self.text = text
        self.root = SuffixTreeNode()
        self.build_tree()

    def build_tree(self):
        # Implementation of Ukkonen's algorithm goes here
        pass
