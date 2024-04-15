class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.root = None

    
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            current_node = self.root
            while True:
                # Right 
                if new_node.data > current_node.data:
                    if current_node.right == None:
                        current_node.right = new_node
                        return
                    else:
                        current_node = current_node.right
                # Left
                else:
                    if current_node.left == None:
                        current_node.left = new_node
                        return
                    else:
                        current_node = current_node.left

    def lookup(self, data):
        current_node = self.root

        if current_node == None:
            return False
        
        if current_node.data == data:
            return True
        elif data > current_node.data:
            current_node = current_node.right
        else:
            current_node = current_node.left

    
    def remove(self,data):
        if self.root == None:
            return False

        currentNode = self.root
        parentNode = None

        while currentNode:
            if data < currentNode.data:
                parentNode = currentNode
                currentNode = currentNode.left
            elif data > currentNode.data:
                parentNode = currentNode
                currentNode = currentNode.right
            elif data == currentNode.data:
                # We have a match, get to work!

                # Option 1: No right child:
                if currentNode.right == None:
                    if parentNode == None:
                        self.root = currentNode.left
                    else:
                        #if parent > current data, make current left child a child of parent
                        if currentNode.data < parentNode.data:
                            parentNode.left = currentNode.left
                        #if parent < current data, make left child a right child of parent
                        elif currentNode.data > parentNode.data:
                            parentNode.right = currentNode.left

                #Option 2: Right child which doesn't have a left child
                elif currentNode.right.left == None:
                    currentNode.right.left = currentNode.left
                    if parentNode == None:
                        self.root = currentNode.right
                    else:
                        #//if parent > current, make right child of the left the parent
                        if currentNode.data < parentNode.data:
                            parentNode.left = currentNode.right
                        #//if parent < current, make right child a right child of the parent
                        elif currentNode.data > parentNode.data:
                            parentNode.right = currentNode.right


                #Option 3: Right child that has a left child
                else:
                    #find the Right child's left most child
                    leftmost = currentNode.right.left
                    leftmostParent = currentNode.right
                    while leftmost.left != None:
                        leftmostParent = leftmost
                        leftmost = leftmost.left

                    #Parent's left subtree is now leftmost's right subtree
                    leftmostParent.left = leftmost.right
                    leftmost.left = currentNode.left
                    leftmost.right = currentNode.right

                    if parentNode == None:
                        self.root = leftmost
                    else:
                        if currentNode.data < parentNode.data:
                            parentNode.left = leftmost
                        elif currentNode.data > parentNode.data:
                            parentNode.right = leftmost
            return True
           

    def print(self,curr_node):
        if curr_node != None:
            self.print(curr_node.left)
            print(str(curr_node.data))
            self.print(curr_node.right)


bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(6)
bst.insert(12)
bst.insert(8)
x = bst.lookup(6)
print(x)
y = bst.lookup(99)
print(y)
bst.print_tree()