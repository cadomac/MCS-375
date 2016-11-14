from __future__ import print_function
from BST import BSTNode,BST
import random
import time

class SplayTree(BST):
    """A splay tree.
    """
    def left_rotate(self, x):
        y = x.right
        if y != self.nil:
            x.right = y.left
            if y.left != self.nil:
                y.left.p = x
            y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        if y != self.nil:
            y.left = x
        x.p = y

    def right_rotate(self, x):
        y = x.left
        if y != self.nil:
            x.left = y.right
            if y.right != self.nil:
                y.right.p = x
            y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        if y != self.nil:
            y.right = x
        x.p = y

    def splay(self, z):
        while (z != self.root):
            if z.p == self.root:
                if z == z.p.left:
                    self.right_rotate(z.p)
                else:
                    self.left_rotate(z.p)
            elif ((z == z.p.left) and (z.p == z.p.p.left)):
                self.right_rotate(z.p.p)
                self.right_rotate(z.p)
            elif ((z == z.p.right) and (z.p == z.p.p.right)):
                self.left_rotate(z.p.p)
                self.left_rotate(z.p)
            elif ((z == z.p.left) and (z.p == z.p.p.right)):
                self.right_rotate(z.p)
                self.left_rotate(z.p)
            elif ((z == z.p.right) and (z.p == z.p.p.left)):
                self.left_rotate(z.p)
                self.right_rotate(z.p)

    def search(self, k):
        x = self.root
        while x != self.nil and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        if k == x.key:
            self.splay(x)
        return x

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
        self.splay(z)

    def delete(self, z):
        x = z
        if z.left == self.nil:
            self.splay(x.p)
            BST.transplant(self, z, z.right)
        elif z.right == self.nil:
            self.splay(x.p)
            BST.transplant(self, z, z.left)
        else:
            y = z.right.minimum(self.nil)
            w = y
            if y.p != z:
                BST.transplant(self, y, y.right)
                y.right = z.right
                y.right.p = y
            BST.transplant(self, z, y)
            y.left = z.left
            y.left.p = y
            self.splay(w)
            

def main():
    start = time.time()
    splayTree = SplayTree()
    print("First insert 20 random nodes into an empty tree and print the tree.")
    for i in range(20):
        n = random.randint(0, 1000)
        splayTree.insert(BSTNode(n, splayTree.nil, splayTree.nil, splayTree.nil))
    print()
    splayTree.print()
    print()

    print("\nThen insert 80 more random nodes into the tree.")
    for i in range(80):
        n = random.randint(0, 1000)
        splayTree.insert(BSTNode(n, splayTree.nil, splayTree.nil, splayTree.nil))
    print("These keys in inorder are: ")
    splayTree.inorder()
    print()

    print("\nNow do 200 searches. ")
    for i in range(200):
        n = random.randint(0, 1000)
        if splayTree.search(n) == splayTree.nil:
            print(n, " not found")
        else:
            print(n, " found")

    print("\nNow search for & delete some nodes.")
    for i in range(2000):
        n = random.randint(0, 1000)
        z = splayTree.search(n)
        if z != splayTree.nil:
            splayTree.delete(z)
            print(n)
    print("The keys in the trees in inorder are now: ")
    splayTree.inorder()
    print()

    print("\nThe final tree looks like this.")
    print()
    splayTree.print()
    print()
    runTime = time.time() - start
    print(runTime)

if __name__ == "__main__":
    main()