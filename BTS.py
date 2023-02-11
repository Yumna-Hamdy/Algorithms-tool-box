import random
import sys

class Node:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value
# data getter
    def get_data(self):
        return self.data
    #data setter
    def set_data(self, value):
        self.data = value

class BST:
    def __init__(self, value):
       self.root= Node(value)
#set root
    def setroot(self, value):
        self.root=Node(value)

    def getroot(self):
        return self.root

    def insertnode(self, value,node):
        #if root is empty
        if self.root is None:
            #set the root if the tree
            self.setroot(value)
#if the value is smaller than the node
        if value<node.data:
# check that the left is empty
           if node.left is None:
               #insert it at the left
               node.left = Node(value)
               return
           self.insertnode(value,node.left)        
            
            
#if the value is bigger than the node
        elif value>node.data:
            # check that the right is empty
            if node.right is None:
                #insert it at the right
                node.right = Node(value)
                  
                return
                 
            self.insertnode(value,node.right)  

    def get_min_itrration(self,root):
        while root.left!= None:
            root=root.left
        return root.data

    def get_min_recursive(self,root):
        if root.left== None:
            return root.data
        return self. get_min_recursive(root.left)


    
    
        
        
        
        


if __name__ == "__main__":
    size = int(input("Enter the size: " )) # get the size of the tree from the user
    if size<=0:
        print("Please enter at least 1 item")
    input= [int(input()) for i in range(size)] #make the user input the tree numbers
    root=Node(input[0])
    tree = BST(input)
    for j in range(size): # putting the elements into the tree
        tree.insertnode((input[j]),root)
    print("\nMinimum Usin Recursion : ", tree.get_min_recursive(root))
    print("Minimum Usin Itertive : ", tree.get_min_itrration(root))
        

                  
