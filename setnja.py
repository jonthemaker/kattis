"""
recursive search and calcutive method,
    through temporary customized binary tree sructure.
"""
class Node:
    def __init__(self, val = -1):
        self.value = val
        self.left = None
        self.right = None
    def makeChild(self, val, depth):
        depth-=1
        self.left = Node(val*2)
        self.right = Node(val*2 + 1)
        if depth > 0:
            self.left.makeChild(val*2, depth)
            self.right.makeChild(val*2 + 1, depth)
    def construct(self, val, walk):
        if bool(walk) == True:
            if (walk[0] == "L"):
                if self.left is None:
                    self.left = Node(2*val)
                self.left.construct(2*val, walk[1:])
            elif (walk[0] == "R"):
                if self.right is None:
                    self.right = Node(2*val + 1)
                self.right.construct(2*val + 1, walk[1:])
            elif (walk[0] == "P"):
                self.construct(val, walk[1:])
            elif (walk[0] == "*"):
                if self.left is None:
                    self.left = Node(2*val)
                self.left.construct(2*val, walk[1:])
                if self.right is None:
                    self.right = Node(2*val + 1)
                self.right.construct(2*val + 1, walk[1:])
                self.construct(val, walk[1:])
    def printWhole(self):
        print(self.value,end=' ')
        if self.left is not None:
            self.left.printWhole()
        if self.right is not None:
            self.right.printWhole()
    def path(self, walk):
        if bool(walk) == True:
            if (walk[0] == "L"):
                rScore = self.left.path(walk[1:])
            elif (walk[0] == "R"):
                rScore = self.right.path(walk[1:])
            elif (walk[0] == "P"):
                rScore = self.path(walk[1:])
            elif (walk[0] == "*"):
                rScore = self.left.path(walk[1:])
                rScore += self.right.path(walk[1:])
                rScore += self.path(walk[1:])
        else:
            return self.value
        return rScore

    def __str__(self):
        return ("Node has a value of "+str(self.value))
    def __repr__(self):
        return str(self.value)
class Tree:
    def __init__(self, depth = 3):
        self.root = Node(1)
        if depth > 0:
            self.root.makeChild(1,depth)
    def construct(self, walk):
        self.root.construct(self.root.value, walk)
    def printALL(self):
        print("Binary Tree Print:")
        self.root.printWhole()
        print("\n-----------------")
    def combinedPath(self, walk):
        return self.root.path(walk)
    def __str__(self):
        return str(self.root.value)



 # for development testing
"""myTree = Tree(0)
print("\nMy Tree:")
print(myTree)
myTree.printALL()
duty = input()
myTree.construct(duty)
print(myTree)
myTree.printALL()
print(myTree.combinedPath(duty))"""
"""myTree = Tree(4)
print("\nMy Tree:")
print(myTree)
myTree.printALL()
print("LRR:",myTree.combinedPath("LRR"))#LRR = 11
print("P*P:",myTree.combinedPath("P*P"))#LRR = 11
print("L*R:",myTree.combinedPath("L*R"))#LRR = 11
print("**:",myTree.combinedPath("**"))#LRR = 11"""


#for kattis
instruction = input()
setnjaTree = Tree(0)
setnjaTree.construct(instruction)
print(setnjaTree.combinedPath(instruction))
