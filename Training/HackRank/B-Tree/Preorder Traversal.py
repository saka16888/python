class Node:
    def __init__(self,data=0,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

    def depth(self):
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
        return max(left_depth,right_depth)+1

    def preorderNode(self):
        tmp=[self.data]
        # print(self.data)
        if self.left : tmp.extend(self.left.preorderNode())
        if self.right : tmp.extend(self.right.preorderNode())
        return tmp

    def inorderNode(self):
        tmp = []
        if self.left: tmp.extend(self.left.preorderNode())
        tmp.extend([self.data])
        if self.right: tmp.extend(self.right.preorderNode())
        return tmp


    def postorderNode(self):
        tmp = [self.data]
        # print(self.data)
        if self.left: tmp.extend (self.left.preorderNode ())
        if self.right: tmp.extend (self.right.preorderNode ())
        return tmp

n1=Node(1)
n2=Node(5)
n3=Node(8)
n4=Node(15)
n5=Node(6,n2,n3)
n6=Node(19,n4)
n7=Node(4,n1,n5)
n8=Node(13,None,n6)
n9=Node(10,n7,n8)
print(n9.depth())

print("Preorder")
print(n9.preorderNode())
mlist=n9.preorderNode()
m=""
for i in mlist:
    m += str(i)+" "

print("Inorder")
print(n9.inorderNode())

print("Postorder")
print(n9.postorderNode())

ret1=True
# ret1=False
ret2=False
ret2=True
print(ret1 and ret2)