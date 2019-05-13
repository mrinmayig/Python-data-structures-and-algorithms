class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
    def insert(self,val):
        if self.val==val:
            return False
        elif self.val>val:
            if self.left:
                return self.left.insert(val)            
            else:
                self.left=Node(val)
                return True
        else:
            if self.right:
                return self.right.insert(val)
            else:
                self.right=Node(val)
                return True
            
    def find(self,data):
        if self.val==data:
            return True
        elif self.val>data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False
            
    def preorder(self):
        if self:
            print(self.val,end=' ')
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()
                
    def postorder(self):
        if self:   
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()          
            print(self.val, end=' ')
            
    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(self.val, end=' ')
            if self.right:
                self.right.inorder()

            
    
class Tree:
    def __init__(self):
        self.root=None
        
    def insert(self,data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root=Node(data)
            return True
        
    def find(self,data):
        if self.root:
            return self.root.find(data)
        else:
            return False
           
    def preorder(self):
        print("Preorder")
        self.root.preorder()
        
    def inorder(self):
        print("Inorder")
        self.root.inorder()
        
    def postorder(self):
        print("Postorder")
        self.root.postorder()