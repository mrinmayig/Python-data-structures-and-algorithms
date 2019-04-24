class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
        
    def print_list(self):
        curr_node=self.head
        while curr_node:
            print(curr_node.data)
            curr_node=curr_node.next
            
    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        
    def insert_after(self,prev_node,data):
        if not prev_node:
            print("Previous node not present in the list")
            return
        new_node=Node(data)
        curr_node=self.head
        while curr_node and curr_node.data!=prev_node:
            curr_node=curr_node.next
        new_node.next=curr_node.next
        curr_node.next=new_node
      
    def delete_node(self,key):
        curr_node=self.head
        if curr_node and curr_node.data==key:
            self.head=curr_node.next
            curr_node=None
            return
        prev=None
        
        while curr_node and curr_node.data!=key:
            prev=curr_node
            curr_node=curr_node.next
        if curr_node is None:
            return
        prev.next=curr_node.next
        curr_node=None
        
    def length(self):
        curr_node=self.head
        count=0
        while curr_node:
            count+=1
            curr_node=curr_node.next
        return count
    
    def reverse(self):
        curr_node=self.head
        prev=None
        while curr_node:
            next=curr_node.next
            curr_node.next=prev
            prev=curr_node
            curr_node=next
        self.head=prev
        
    def len_recursive(self,node):
        if node is None:
            return 0
        return 1+self.len_recursive(node.next)
    
    def node_swap(self,key_1,key_2):
        if key_1==key_2:
            return
        prev_1=None
        curr_1=self.head
        while curr_1 and curr_1.data!=key_1:
            prev_1=curr_1
            curr_1=curr_1.next
        prev_2=None
        curr_2=self.head
        while curr_2 and curr_2.data!=key_2:
            prev_2=curr_2
            curr_2=curr_2.next
        if not curr_1 or not curr_2:
            return
        if prev_1:
            prev_1.next=curr_2
        else:
            self.head=curr_2
        if prev_2:
            prev_2.next=curr_1
        else:
            self.head=curr_1
        curr_1.next,curr_2.next=curr_2.next,curr_1.next
        
    def reverse_recursive(self):
        def _reverse_recursive_(curr, prev):
            if not curr:
                return prev
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
            return _reverse_recursive_(curr,prev)
        self.head=_reverse_recursive_(curr=self.head,prev=None)
        
    def merge_sorted(self,llist):
        p = self.head 
        q = llist.head
        s = None
    
        if not p:
            return q
        if not q:
            return p
       
        if p and q:
            if p.data < q.data:  
                s = p 
                p = s.next

            elif q.data < p.data: 
                s = q
                q = s.next  
            new_head=s  
            
        while p and q:
            if p.data < q.data:
                s.next = p 
                s = p 
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q 
        if not q:
            s.next = p 
        self.head = new_head 
        llist.head = None
        return new_head
    
    def remove_duplicates(self):
        curr=self.head
        prev=None
        dup_values=dict()
        while curr:
            if curr.data in dup_values:
                prev.next=curr.next
                curr=None
            else:
                dup_values[curr.data]=1
                prev=curr
            curr=prev.next
            
    def print_nth_from_last(self,n):
        p=self.head
        q=self.head
        count=0
        while q and count<n:
            q=q.next
            count+=1
        if not q:
            print(str(n)+"is greater than the number of nodes in list")
            return
        while p and q:
            p=p.next
            q=q.next
        return p.data
    
    def count_occurr(self,data):
        curr=self.head
        occur=dict()
        while curr:
            if curr.data in occur:
                occur[curr.data]+=1
                curr=curr.next
            else:
                occur[curr.data]=1
                curr=curr.next
        return occur[data]
    
    def count_occur(self,data):
        count=0
        curr=self.head
        while curr:
            if curr.data==data:
                count+=1
            curr=curr.next
        return count
    
    def rotate(self,k):
        p=self.head
        q=self.head
        prev=None
        count=0
        while p and count<k:
            prev=p
            p=p.next
            q=q.next
            count+=1
        p=prev
        
        while q:
            prev=q
            q=q.next
        q=prev
        
        q.next=self.head
        self.head=p.next
        p.next=None    
        
    def is_palindrome(self):
        s=""
        p=self.head
        while p:
            s+=p.data
            p=p.next
        return s==s[::-1]
    
    def is_palin(self):
        s=[]
        p=self.head
        while p:
            s.append(p.data)
            p=p.next
        p=self.head
        while p:
            data=s.pop()
            if p.data!=data:
                return False
            p=p.next
        return True
    
    def move_tail_to_head(self):
        p=self.head
        prev=None
        while p.next:
            prev=p
            p=p.next
        p.next=self.head
        prev.next=None
        self.head=p