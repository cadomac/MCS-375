from __future__ import print_function
import random
import time

class BSTNode:
    """A binary search tree node.
    """
    def __init__(self, key=None, left=None, right=None, p=None):
        self.key = key
        self.left = left
        self.right = right
        self.p = p
 
    def __str__(self):
        return str(self.key)

    def inorder(self, nil):
        if self != nil:
            self.left.inorder(nil)
            print(self.key, end=' ')
            self.right.inorder(nil)

    def search(self, k, nil):
        x = self
        while x != nil and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def minimum(self, nil):
        x = self
        while x.left != nil:
            x = x.left
        return x

    def maximum(self, nil):
        x = self
        while x.right != nil:
            x = x.right
        return x

    def successor(self, nil):
        if self == nil:
            return self
        if self.right != nil:
            return self.right.minimum(nil)
        x = self
        y = self.p
        while y != nil and x == y.right:
            x = y
            y = y.p
        return y

    """Print the tree rooted at self in a visually readable format.
       For debugging purpose only.
    """
    def print(self, nil, level):
        if self != nil:
            self.right.print(nil, level+1)
            for i in range(level):
                print("    ", end='')
            print("%4d" % self.key)
            self.left.print(nil, level+1)

class BST:
    """A binary search tree.
    """
    def __init__(self, bst=None):
        if bst == None:
            self.nil = BSTNode()
            self.nil.left = self.nil.right = self.nil.p = self.nil
            self.root = self.nil
        else:
            self.root = bst.root
            self.nil = bst.nil

    def inorder(self):
        self.root.inorder(self.nil)

    def search(self, k):
        return self.root.search(k, self.nil)

    def minimum(self):
        return self.root.minimum(self.nil)

    def maximum(self):
        return self.root.maximum(self.nil)

    def insert(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def transplant(self, u, v):
        if u.p == self.nil:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v != self.nil:
            v.p = u.p

    def delete(self, z):
        if z.left == self.nil:
            self.transplant(z, z.right)
        elif z.right == self.nil:
            self.transplant(z, z.left)
        else:
            y = z.right.minimum(self.nil)
            if y.p != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y

    """Print this tree in a visually readable format.
       For debugging purpose only.
    """
    def print(self):
        self.root.print(self.nil, 0)

def main():
    start = time.time()
    bst = BST()
    print("First insert 20 random nodes into an empty tree and print the tree.")
    for i in range(20):
        n = random.randint(0, 1000)
        bst.insert(BSTNode(n, bst.nil, bst.nil, bst.nil))
    print()
    bst.print()
    print()

    print("\nThen insert 80 more random nodes into the tree.")
    for i in range(80):
        n = random.randint(0, 1000)
        bst.insert(BSTNode(n, bst.nil, bst.nil, bst.nil))
    print("These keys in inorder are: ")
    bst.inorder()
    print()

    print("\nNow do 200 searches. ")
    for i in range(200):
        n = random.randint(0, 1000)
        if bst.search(n) == bst.nil:
            print(n, " not found")
        else:
            print(n, " found")

    print("\nNow search for & delete some nodes.")
    for i in range(2000):
        n = random.randint(0, 1000)
        z = bst.search(n)
        if z != bst.nil:
            bst.delete(z)
    print("The keys in the trees in order are now: ")
    bst.inorder()
    print()

    print("\nNow print the keys in order again by calling minimum, then repeatedly calling successor.")
    x = bst.minimum()
    print(x, end=' ')
    x = x.successor(bst.nil)
    while x != bst.nil:
        print(x, end=' ')
        x = x.successor(bst.nil)
    print()

    print("\nThe maximum key is: ")
    print(bst.maximum())

    print("\nThe final tree looks like this.")
    print()
    bst.print()
    print()
    runTime = time.time() - start
    print(runTime)

if __name__ == "__main__":
    main()
