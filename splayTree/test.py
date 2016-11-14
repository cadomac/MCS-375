## BST vs. SplayTree Test Function ##

from BST import *
from CM_SplayTree import *
import time
import random

nodeValues = []
searchValues = []
deleteValues = []

def bstAlg():
    bst = BST()
    for i in range(20):
        bst.insert(BSTNode(nodeValues[i], bst.nil, bst.nil, bst.nil))
    print()
    for i in range(20, 100):
        bst.insert(BSTNode(nodeValues[i], bst.nil, bst.nil, bst.nil))
    print("These keys in inorder are: ")
    bst.inorder()
    print()

    print("\nNow do 200 searches. ")
    for i in range(200):
        n = searchValues[i]
        if bst.search(n) == bst.nil:
            print(n, " not found")
        else:
            print(n, " found")

    print("\nNow search for & delete some nodes.")
    for i in range(2000):
        z = bst.search(deleteValues[i])
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

def splAlg():
    splayTree = SplayTree()
    for i in range(20):
        splayTree.insert(BSTNode(nodeValues[i], splayTree.nil, splayTree.nil, splayTree.nil))
    print()
    for i in range(20, 100):
        splayTree.insert(BSTNode(nodeValues[i], splayTree.nil, splayTree.nil, splayTree.nil))
    print("These keys in inorder are: ")
    splayTree.inorder()
    print()

    print("\nNow do 200 searches. ")
    for i in range(200):
        n = searchValues[i]
        if splayTree.search(n) == splayTree.nil:
            print(n, " not found")
        else:
            print(n, " found")

    print("\nNow search for & delete some nodes.")
    for i in range(2000):
        n = deleteValues[i]
        z = splayTree.search(n)
        if z != splayTree.nil:
            splayTree.delete(z)
    print("The keys in the trees in inorder are now: ")
    splayTree.inorder()
    print()

    print("\nThe final tree looks like this.")
    print()
    splayTree.print()
    print()

def populateValues():
    for i in range(100):
        nodeValues.append(i)
    for i in range(1000):
        k = random.randint(0, 1000)
        searchValues.append(k)
    for i in range(2000):
        m = random.randint(0, 500)
        deleteValues.append(m)

populateValues()

start_time = time.time()
if __name__ == '__main__':
    bstAlg()
bstTime = (time.time() - start_time)


new_time = time.time()
if __name__ == '__main__':
    splAlg()
splTime = (time.time() - new_time)
print("BST: %s seconds ---" % bstTime)
print("SplayTree: %s seconds ---" % splTime)