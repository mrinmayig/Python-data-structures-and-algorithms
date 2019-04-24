class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class CircularLList:
    
    def __init__(self):
        self.head=None
        
    def append(self,data):
        if not self.head:
            self.head=Node(data)
            self.head.next=self.head
            
        else:
            new_node=Node(data)
            curr=self.head
            while curr.next!=self.head:
                curr=curr.next
            curr.next=new_node
            new_node.next=self.head
            
    def print_list(self):
        curr=self.head
        while curr:
            print(curr.data,end='-->')
            curr=curr.next
            if curr==self.head:
                break
                
    def prepend(self,data):
        new_node=Node(data)
        curr=self.head
        new_node.next=self.head
        if not self.head:
            new_node.next=new_node
            
        else:
            while curr.next!=self.head:
                curr=curr.next
            curr.next=new_node
        self.head=new_node
    
    def remove(self,key):
                
        if self.head.data==key:
            curr=self.head
            while curr.next!=self.head:
                curr=curr.next
            curr.next=self.head.next
            self.head=self.head.next
        else:
            curr=self.head
            prev=None
            while curr.next!=self.head:
                prev=curr
                curr=curr.next
                if curr.data==key:
                    prev.next=curr.next
                    curr=curr.next
        
        if self.head==self.head.next and self.head.data==key:
            self.head=None    
    
    def len_of_list(self):
        curr=self.head
        count=0
        while curr:
            count+=1
            curr=curr.next
            if curr==self.head:
                break
        return count
    
    def split_list(self):
        size=self.len_of_list()
        
        if size==0:
            return None
        if size==1:
            return self.head
        mid=size//2
        count=0
        prev=None
        curr=self.head
        while curr and count<mid:
            count+=1
            prev=curr
            curr=curr.next
        prev.next=self.head
        
        split_cllist=CircularLList()
        while curr.next!=self.head:
            split_cllist.append(curr.data)
            curr=curr.next
        split_cllist.append(curr.data)
        
        self.print_list()
        print('\n')
        split_cllist.print_list()
        
    def remove_node(self,node):
                
        if self.head.data==node:
            curr=self.head
            while curr.next!=self.head:
                curr=curr.next
            curr.next=self.head.next
            self.head=self.head.next
        else:
            curr=self.head
            prev=None
            while curr.next!=self.head:
                prev=curr
                curr=curr.next
                if curr.data==node:
                    prev.next=curr.next
                    curr=curr.next
        
        if self.head==self.head.next and self.head.data==node:
            self.head=None
            
    def is_circular(self,input_list):
        curr=input_list.head
        while curr.next:
            curr=curr.next
            if curr.next==input_list.head:
                return True           
        return False