class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data

class Solution:
    def insert(self, root, data):
        if root == None:
            # print("data",data)
            return Node (data)
        else:
            if data <= root.data:
                cur = self.insert (root.left, data)
                root.left = cur
            else:
                cur = self.insert (root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        left_height = self.getHeight (root.left) if root.left else 0
        right_height = self.getHeight (root.right) if root.right else 0
        return max (left_height, right_height) + 1

    def preorder(self,root):
        tmp=root.data
        if root.left : tmp.extend(root.left.preorderNode())
        if root.right: tmp.extend (root.right.preorderNode ())
        return tmp

    def check_binary_search_tree(self,root):
        data = root.data
        print('data =',data)
        if root.left:
            if root.data <= root.left.data:
                return False
            else:
                ret1 = self.check_binary_search_tree(root.left)
                # print('ret1 =',ret1)
        else:
            ret1 = True
        if root.right:
            if (root.data >= root.right.data):
                return False
            else:
                ret2 = self.check_binary_search_tree(root.right)
                # print('ret2 =',ret2)
        else:
            ret2 = True
        return (ret1 and ret2)


myTree = Solution ()
root = None

# T = int(input())
# for i in range (T):
#     data = int(input())
#     root = myTree.insert (root, data)
# data="1 2 4 3 5 6 7"
data="9 10 2 1 4 3 5 6 7"
for i in data.split():
    root = myTree.insert (root, int(i))

height = myTree.getHeight(root)
print('height = ',height)

print(myTree.check_binary_search_tree(root))