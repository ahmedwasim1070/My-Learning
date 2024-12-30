import ctypes
import sys
class MeralList:

    def __init__(self):
        self.size=1
        self.n=0
        # create a c type array with size= self.size
        self.A = self.__crt_array(self.size)    

    def __len__(self):
        return self.n

    def append(self,item):
        if self.n==self.size:
            # resize
            self.__resize(self.size*2)
        
        # append
        self.A[self.n]=item
        self.n=self.n+1

    def pop(self):
        if(self.n==0):    
            print("Error List is already Empty")
        else:    
            print(self.A[self.n-1])
            self.n=self.n-1
    
    def clear(self):
        self.n=0
        self.size=0
    
    def find(self,fndVal):
        for i in range(self.n):
            if(self.A[i]==fndVal):
                return i 
                break
        return "Your ",fndVal,"Not found"   
    
    def replace(self,index,value):
        self.A[index]=value

    def insert(self,index,value):
        if(self.n==self.size):
            self.__resize(self.size*2)
        for i in range(self.n,index,-1):
            self.A[i]=self.A[i-1]
        self.A[index]=value
        self.n=self.n+1

    def __delitem__(self,pos):
        if 0<= pos < self.n:
            for i in range(pos,self.n-1):
                self.A[i]=self.A[i+1]
            self.n=self.n-1

    def remove(self,item):
        pos=self.find(item)
        if(type(pos)==int):
            self.__delitem__(pos)
        else:
            return pos
    
    def index_picking(self,index):
        result=""
        for i in range(0,index+1):
            if i==self.n:
                return
            result=result+str(self.A[i])+","
        return result[:-1]

    def len_byte(self,value):
        idx=self.find(value)
        return sys.getsizeof(self.A[idx])
    
    def max(self):
        max =  self.A[0]
        for i in range(1,self.n):
            if self.A[i] > max:
                max=self.A[i]
        return max
    
    def __str__(self):
        result=""    
        for i in range(self.n):
            result=result+str(self.A[i])+","
        return "[" + result[:-1] + "]"    

    def __resize(self,new_capacity):
        #  create a new array with new capacity
        B=self.__crt_array(new_capacity)
        self.size=new_capacity
        # copy the content of A to B
        for i in range(self.n):
            B[i]=self.A[i]
        self.A=B
    
    def __getitem__(self,index):
        if(index<self.n):
            return self.A[index]
        print("Enter a Valid Number")
    
    def __crt_array(self,capacity):
        # Create a C type array with capacity with size capacity
        return(capacity*ctypes.py_object)()

# L=MeralList()
# L.append(5)
# L.append(2)
# L.append(3)
# print(L.max())
# print(L)
# Arrays Ended




# Linked List 

# Creating Node
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
    
# Creating Linked List
class LinkedList:
    def __init__(self):
        # Empty Linked List
        self.head=None
        # No of Node's in the Linked list
        self.n=0

    def __len__(self):
        return self.n

    def __getitem__(self,idx):
        # curr=self.head
        # if idx==0:
        #     return curr.data
        # if idx<self.n:
        #     for i in range(0,idx):
        #         curr=curr.next
        #     return curr.data
        # OR
        curr=self.head
        i=0
        while curr!=None:
            if i==idx:
                return curr.data
            i+=1
            curr=curr.next
        return None
        

    def insert_head(self,value):
        # New node 
        new__node = Node(value)
        # create connnection
        new__node.next = self.head
        # reasign head 
        self.head=new__node
        # increament n 
        self.n=self.n+1
    
    def append(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
            self.n=self.n+1
            return
        curr=self.head
        while curr.next!=None:
            curr=curr.next
        # curr is on the last node 
        curr.next=new_node
        self.n=self.n+1

# Traverse
    def __str__(self):
        curr= self.head
        result=""
        while curr!=None:
            result= result+str(curr.data) +"->"
            curr=curr.next
        return result [:-2]

    def insert_after(self,after,value):
        new_node=Node(value)
        curr=self.head
        while curr!=None:
            if curr.data==after:
                break
            curr=curr.next
        # case 1 break -> item's found -> curr -> not none
        if curr!=None:
            # Logic
            new_node.next=curr.next
            curr.next=new_node
            self.n=self.n+1
        else:
            return "Item Not found!"
        # case 2 loop completed -> item's found -> cur -> None 

    def clear(self):
        self.head=None
        self.n=0
    
    def del_head(self):
        if self.head==None:
            print("List already empty")
        else:
            self.head=self.head.next
            self.n=self.n-1
    
    def pop(self):
        curr=self.head
        if curr==None:
            return "Empty linked list ! "
        if curr.next ==None:
            self.del_head()
            return
        while curr.next.next!=None:
            curr=curr.next
        curr.next=None
        self.n=self.n-1
    
    def remove(self,value):
        curr=self.head
        if curr==None:
            return "List is already empty"
        if curr.data==self.head:
            self.del_head()
            self.n=self.n-1
            return
        while curr.next!=None:
            if curr.next.data==value:
                break
            curr=curr.next
        if curr.next==None:
            return "Item Not found ! "
        else:
            curr.next=curr.next.next
            self.n=self.n-1        
    
    def search(self,value):
        curr=self.head
        i=0
        while curr!=None:
            if curr.data==value:
                return "Item found at Index: " , i 
            curr=curr.next
            i+=1
        return value, "Not Found"    
    
    def replace(self,value,val):
        curr=self.head
        while curr!=None:
            if curr.data==value:
                curr.data=val
                return True
            curr=curr.next
        return False

    def max(self,value):
        curr=self.head
        tmp=curr
        while curr!=None:
            if curr.data > tmp.data:
                tmp=curr 
            curr=curr.next
        self.replace(tmp.data,value)
        return True

    def odd_sum(self):
        curr=self.head
        sum=1
        while curr!=None:
            if curr.data%2!=0:
                sum*=curr.data
            curr=curr.next
        return sum
        # Or
        # curr=self.head
        # couter=0
        # result=0
        # while curr!=None:
        #     if couter%2!=0:
        #         result=result+curr.data
        #     couter+=1
        #     curr=curr.next
        # return result
    
    def reverse(self):
        prev_node=None
        curr=self.head
        while curr!=None:
            next_node=curr.next
            curr.next=prev_node
            prev_node=curr
            curr=next_node
        self.head=prev_node

    def symbol_rm(self):
        curr=self.head
        while curr.next!=None:
            if curr.data=="/" or curr.data=="*":
                curr.data=" "
                if curr.next.data=="*" or curr.next.data=="/":
                    curr.next.next.data=curr.next.next.data.capitalize()
                    self.remove(curr.next.data)
            curr=curr.next
    
# L=LinkedList()
# L.append(1)
# L.append(2)
# L.append(4)
# print(L)
# f=LinkedList()
# f.append(1)
# f.append(3)
# f.append(4)
# Linked List Ends Here.


# Creating Stacks with Linked List.
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class Stacks:
    def __init__(self):
        self.top=None
        self.n=0
    def size(self):
        return self.n
    def isempty(self):
        return self.top==None
    def push(self,value):
        new_stack=Node(value)
        new_stack.next=self.top
        self.top=new_stack
        self.n=self.n+1
    def pop(self):
        if self.isempty():
            return "Already Empty!"
        else:
            poped_val=self.top.data
            self.top=self.top.next
            self.n=self.n-1
            return poped_val
    def peak(self):
        if(self.isempty()):
            return "No nodes in the list ! "
        return self.top.data            
    def __str__(self):
        temp=self.top
        res=""
        while temp!=None:
            res=res+str(temp.data)
            temp=temp.next
        return res

# L=Stacks()
# L.push(1)
# L.push(2)
# L.push(3)
# print(L.pop())
# print(L)

# Reversing Stacks
def reverse_string(text):
    s=Stacks()
    for i in text:
        s.push(i)
    res=""
    while s.isempty()==False:
        res=res+s.top.data
        s.pop()
    return res

# Undo Redo
def text_editor(text,pattern):
    u=Stacks()
    r=Stacks()
    for i in text:
        u.push(i)
        print(u)
    for i in pattern:
        if i=="u":
            data=u.pop()
            r.push(data)
        elif i=="r":
            data=r.pop()
            if data!="Already Empty!":
                u.push(data)
    res=""
    while (not u.isempty()):
        res=u.pop()+res
    print(res)

# Celebrity Problem
L=[
    [0,0,1,1],
    [0,0,1,0],
    [0,0,1,0],
    [0,0,1,0]
]
def fnd_celb(L):
    s=Stacks()
    for i in range(len(L)):
        s.push(i)
    while s.size() >=2:
        a=s.pop()
        b=s.pop()
        if L[a][b] == 0 : 
            # b is not an celebrity
            s.push(a)
        else:
            # a is not an celebrity
            s.push(b)
    celeb=s.pop()
    for i in range(len(L)):
        if i !=celeb:
            if L[i][celeb]==0 or L[celeb][i]==1:
                print("No one is celebrity")
                return
        if i==celeb:
            if L[i][celeb]==1:
                print("No one is celebrity")
                return
    print("The celeb is ",celeb)           
# fnd_celb(L)

# Chceking the brackets in the equation
eq="(a+b)+(a+b)"
def chk_bra(eq):
    s=Stacks()
    b=Stacks()
    for i in eq:
        s.push(i)
    while not s.isempty():
        prev=s.pop()
        if prev=="]"or prev=="}" or prev==")":
            b.push(prev)
        if prev=="[" or prev=="{" or prev=="(":
            if b.isempty()==False:
                if prev=="(":
                    prev=")"
                    b.pop()
                if prev=="{":
                    prev="}"
                    b.pop()
                if prev=="[":
                    prev="]"
                    b.pop()
            else:
                b.push(prev)
    if b.isempty()==True:
        return True
    else:
        return False
# print(chk_bra(eq))

# Creating Stack in Arrays
class stacks:
    def __init__(self,size):
        self.size=size
        self.stack=[None]*self.size
        self.top=-1
    def push(self,value):
        if self.top==self.size-1:
            print("Overflow")
        else:
            self.top+=1
            self.stack[self.top]=value
    def pop(self):
        if self.stack[self.top]==None:
            print("Already Empty")
        else:
            data=self.stack[self.top]
            self.top-=1
            return data
    def traverse(self):
        for i in range(self.top+1):
            print(self.stack[i],end='')
# s=Stacks(5)
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
# s.push(5)
# s.pop()
# s.traverse()

class nodes:
    def __init__(self,value):
        self.data=value
        self.next=None
class queues:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,value):
        newQ=Node(value)
        if self.front==None:
            self.front=newQ
            self.rear=self.front
            return
        else:
            self.rear.next=newQ
            self.rear=newQ
    def dequeue(self):
        if self.front==None:
            return None
        else:
            self.front=self.front.next
    def isempty(self):
        return self.front==None
    def __len__(self):
        temp=self.front
        count=1
        while temp.next!=None:
            count+=1
            temp=temp.next
        return count
    def traverse(self):
        temp=self.front
        while temp!=None:
            print(temp.data)
            temp=temp.next
    def frnt_item(self):
        if self.front!=None:
            return self.front.data
        else:
            return "Empty"
    def rare_item(self):
        if self.rare!=None:
            return self.rare.data
        else:
            return "No rare function exsist"
# Q=queues()
# Q.enqueue(0)
# Q.enqueue(1)
# Q.enqueue(2)
# Q.dequeue()
# Q.traverse()


# Problem
# You have 2 stacks from 2 stacks you need to make queueu
class Queueusingstacks:
    def __init__(self):
        self.stack1=Stacks()
        self.stack2=Stacks()
    def stack_enqueue(self,item):
        if self.stack1.isempty()==True:
            self.stack1.push(item)
        else:
            while not self.stack1.isempty():
                prev=self.stack1.pop()
                self.stack2.push(prev)
            self.stack2.push(item)
            while not self.stack2.isempty():
                nxt=self.stack2.pop()
                self.stack1.push(nxt)
        print(self.stack1)
    def stack_dequeue(self):
        while not self.stack1.isempty():
            prev=self.stack1.pop()
            self.stack2.push(prev)
        self.stack2.pop()
        while not self.stack2.isempty():
            nxt=self.stack2.pop()
            self.stack1.push(nxt)
        print(self.stack1)

# qs=Queueusingstacks()
# qs.stack_enqueue(1)
# qs.stack_enqueue(2)
# qs.stack_enqueue(3)
# qs.stack_dequeue()


# Hashing
# Open addressing Technique
def rd_hash(input_str):
    hash_val=0
    for i in input_str:
        hash_val=hash_val*31+ord(i)
    return hash_val & 0xFFFFF
class Dictionary:
    def __init__(self,size):
        self.size=size
        self.slots=[None]*self.size
        self.data=[None]*self.size
    def put(self,key,value):
        hash_value=self.hash_fun(key)
        if self.slots[hash_value]==None:
            self.slots[hash_value]=key
            self.data[hash_value]=value
        else:
            if self.slots[hash_value]==key:
                self.data[hash_value]=value
            else:
                attempt=1
                new_hash_value=self.rehash(hash_value,attempt)    
                while self.slots[new_hash_value]!=None and self.slots[new_hash_value]!=key:
                    new_hash_value=self.rehash(new_hash_value,attempt)
                    attempt+=1
                if self.slots[new_hash_value]==None:
                    self.slots[new_hash_value]=key
                    self.data[new_hash_value]=value
                else:
                    self.data[new_hash_value]=value
    def get(self,key):
        start_pos=self.hash_fun(key)
        curr_pos=start_pos
        attempt=1
        while self.slots[curr_pos]!=None:
            if self.slots[curr_pos]==key:
                return self.data[curr_pos]
            curr_pos=self.rehash(start_pos,attempt)
            attempt+=1
            if curr_pos==start_pos:
                return "Item not found!"
        return "Not found!"
    def __str__(self):
        for i in range(len(self.slots)):
            if self.slots[i]!=None:
                print(self.slots[i],":",self.data[i],end=" ")
        return ""
    def __getitem__(self,key):
        return self.get(key)
    def __setitem__(self,key,value):
        self.put(key,value)
    def hash_fun(self,key):
        return rd_hash(key)%self.size
    def rehash(self,old_hash,attempt):
        return (old_hash+attempt**2)%self.size
    
# D1=Dictionary(3)
# D1.put("python",100)
# D1["java"]=20
# D1["hello"]=12
# D1["hello"]=14
# print(D1.slots)

# Clossed Addressing Technique

# In closed addressing technique linked is first created
# class Node:
#     def __init__(self,key,value):
#         self.key=key
#         self.value=value
#         self.next=None
# class LL:
#     def __init__(self):
#         self.head=None
#         self.n=0
#     def append(self,key,value):
#         new_node=Node(key,value)
#         if self.head==None:
#             self.head=new_node
#             self.n+=1
#         else:
#             temp=self.head
#             while temp.next!=None:
#                 temp=temp.next
#             temp.next=new_node
#             self.n+=1
#     def remove(self,key):
#         temp=self.head
#         if self.head.key==key:
#             self.head=temp.next
#             self.n-=1
#             return
#         while temp.next!=None:
#             if temp.next.key==key:
#                 break
#             temp=temp.next
#         temp.next=temp.next.next
#         self.n-=1
#     def traverse(self):
#         temp=self.head
#         while temp!=None:
#             print("->","Key : ",temp.key,"-> Val =",temp.value,end="")
#             temp=temp.next
#     def search(self,key):
#         temp=self.head
#         count=0
#         while temp is not None:
#             if temp.key==key:
#                 return count
#             temp=temp.next
#             count+=1
#         return -1
#     def get_node_at_index(self,index):
#         temp=self.head
#         count=0
#         while temp is not None:
#             if count==index:
#                 return temp
#             temp=temp.next
#             counter+=1
# class Dictionary:
#     def __init__(self,capactiy):
#         self.capacity=capactiy
#         self.size=0
#         # Create array of LL
#         self.buckets=self.make_array(self.capacity)
#     def make_array(self,capacity):
#         L=[]
#         for i in range(capacity):
#             L.append(LL())
#         return L
#     def put(self,key,value):
#         bucket_index=self.hash_fuction(key)
#         node_index=self.get_node_index(bucket_index,key)
#         if node_index==-1:
#             self.buckets[bucket_index].append(key,value)
#             self.size+=1
#         else:
#             node=self.buckets[bucket_index].get_node_at_index(node_index)
#             node.value=value
#     def get(self,key):
#         bucket_index=self.hash_fuction(key)
#         node_index=self.get_node_index(bucket_index,key)
#         if node_index==-1:
#             return "Does not exsist"
#         else:
#             node=self.buckets[bucket_index].get_node_at_index(node_index)
#             return "Key = "+node.key,"Value = "+str(node.value),bucket_index
#     def traverse(self):
#         for i in range(len(self.buckets)):
#             res=self.buckets[i]
#             return "---->",i,res.traverse()
#     def get_node_index(self,bucket_index,key):
#         node_index=self.buckets[bucket_index].search(key)
#         return node_index
#     def hash_fuction(self,key):
#         return (rd_hash(key))%self.capacity


# Closed Hashing technique using Load factor rehashing
class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
class LL:
    def __init__(self):
        self.head=None
        self.n=0
    def size(self):
        return self.n
    def append(self,key,value):
        new_node=Node(key,value)
        if self.head==None:
            self.head=new_node
            self.n+=1
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=new_node
            self.n+=1
    def remove(self,key):
        temp=self.head
        if self.head.key==key:
            self.head=temp.next
            self.n-=1
            return
        while temp.next!=None:
            if temp.next.key==key:
                break
            temp=temp.next
        temp.next=temp.next.next
        self.n-=1
    def traverse(self):
        res=""
        temp=self.head
        while temp!=None:
            res=res+"Key : "+str(temp.key)+" , Value : "+str(temp.value)+" -> "
            temp=temp.next
        return res
    def search(self,key):
        temp=self.head
        count=0
        while temp is not None:
            if temp.key==key:
                return count
            temp=temp.next
            count+=1
        return -1
    def get_node_at_index(self,index):
        temp=self.head
        count=0
        while temp is not None:
            if count==index:
                return temp
            temp=temp.next
            count+=1
class Dictionary:
    def __init__(self,capactiy):
        self.capacity=capactiy
        self.size=0
        # Create array of LL
        self.buckets=self.make_array(self.capacity)
    def make_array(self,capacity):
        L=[]
        for i in range(capacity):
            L.append(LL())
        return L
    def put(self,key,value):
        bucket_index=self.hash_fuction(key)
        node_index=self.get_node_index(bucket_index,key)
        if node_index==-1:
            self.buckets[bucket_index].append(key,value)
            self.size+=1
            lamda=self.size/self.capacity
            if lamda >=2:
                self.rehash_function()
        else:
            node=self.buckets[bucket_index].get_node_at_index(node_index)
            node.value=value
    def get(self,key):
        bucket_index=self.hash_fuction(key)
        node_index=self.get_node_index(bucket_index,key)
        if node_index==-1:
            return "Does not exsist"
        else:
            node=self.buckets[bucket_index]
            node=node.get_node_at_index(node_index)
            print("Key : " + str(node.key)+ " , Value : "+str(node.value))
    def delete(self,key):
        bucket_index=self.hash_fuction(key)
        node_index=self.get_node_index(bucket_index,key)
        if node_index!=-1:
            temp=self.buckets[bucket_index].get_node_at_index(node_index-1)
            temp.next=temp.next.next
        else:
            return "Invalid value!"
    def traverse(self):
        for i in range(len(self.buckets)):
            res=self.buckets[i]
            print(res.traverse()[:-3])
    def get_node_index(self,bucket_index,key):
        node_index=self.buckets[bucket_index].search(key)
        return node_index
    def hash_fuction(self,key):
        return (rd_hash(key))%self.capacity
    def rehash_function(self):
        self.capacity=self.capacity*2
        old_buckets=self.buckets
        self.size=0
        self.buckets=self.make_array(self.capacity)
        for i in old_buckets:
            temp=i.head
            while temp is not None:
                self.put(temp.key,temp.value)
                temp=temp.next
# clo=Dictionary(2)
# clo.put("pakistan",92)
# clo.put("india",91)
# clo.put("america",1)
# clo.put("united kingdom",2)
# clo.put("korea",44)
# clo.put("nigeria",1)
# clo.put("jamaica",82)
# clo.put("china",86)
# clo.put("scotland",12)
# clo.get("america")

# Searching

# Linear Searching
def linear_search(arr,item):
    for i in range(len(arr)):
        if arr[i]==item:
            return i
    return -1

# Binary Searching
# def binary_search(arr,low,high,item):
#     if low<=high:
#         mid=(low+high)//2
#         if arr[mid]==item:
#             return item
#         elif arr[mid]>item:
#             return binary_search(arr,low,mid-1,item)
#         else:
#             return binary_search(arr,mid+1,high,item)
#     else:
#         return -1

def binary_search(arr,item):
    high=len(arr)-1
    low=0
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==item:
            return item,"found at index : ",mid
        elif arr[mid]>item:
            high=mid-1
        elif arr[mid]<item:
            low=mid+1
    return -1  



# Sortions in python
def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True

# Monkey sort
import random
def monkey_sort(arr):
    count=0
    while not is_sorted(arr):
        random.shuffle(arr)
        count+=1
    print(arr,count)


# Sleep sort
# import time
# def sleep_sort(arr,count,arr2):
#     for i in range(len(arr)):
#         if arr[i]==count:  
#             arr2.append(count)
#     print(arr2,count)
# arr=[2,1,3,7]
# arr2=[]
# count=0
# while len(arr)>len(arr2):
#     sleep_sort(arr,count,arr2)
#     count+=1
#     time.sleep(1)

import time
import threading
def sleep_and_append(number, result):
    time.sleep(number)
    result.append(number)
def sleep_sort(arr):
    result = []
    threads = []
    for number in arr:
        thread = threading.Thread(target=sleep_and_append, args=(number, result))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
        return result


# Bubble sort : 
def bubble_sort(arr):
    while not is_sorted(arr):
        for i in range(0,len(arr)-1):
            fst=arr[i]
            nxt=arr[i+1]
            if fst>nxt:
                arr[i]=nxt
                arr[i+1]=fst
    return arr
	
def bubble_sort(arr):
    for i in range(len(arr)-1):
        flags=0
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                flags=1
        if flags==0:
            break
    print(arr)

# Selection Sort : 
def selection_sort(arr):
    for i in range(len(arr)-1):
        mini=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[mini]:
                mini=j
        arr[i],arr[mini]=arr[mini],arr[i]
    print(arr)


# Merge Sort : 
def merged_sort(arr1,arr2,arr):
    i=j=k=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            arr[k]=arr1[i]
            i+=1
        else:
            arr[k]=arr2[j]
            j+=1
        k+=1
    while i<len(arr1):
        arr[k]=arr1[i]
        k+=1
        i+=1
    while j<len(arr2):
        arr[k]=arr2[j]
        k+=1
        j+=1
    return

def merge_sort(arr):
    if len(arr)==1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merged_sort(left,right,arr)

arr=[11,2,1,3,45,7]
merge_sort(arr)


# Tree (Non-Linear data structure)
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
def build_tree():
    root=TreeNode("Electronics")
    laptop=TreeNode("Laptop")
    laptop.add_child("Mac")
    laptop.add_child("Windows")
    laptop.add_child("linux")

# # Example Tree structure of the company
class TreeNode:
    def __init__(self,data,post):
        self.data=data
        self.post=post
        self.children=[]
        self.parent=None
    def add_child(self, child):
        child.parent = self
        self.children.append(child) 
    def print_tree(self,level=0):
        space=" "*(level*4)
        prefix=space+"|__" if self.parent else ""
        print(f"{prefix}{self.data} ({self.post})")
        if self.children:
            for child in self.children:
                child.print_tree(level+1)

def build_tree():
    root=TreeNode("Ahmad","CEO")
    cto=TreeNode("George","CTO")
    ih=TreeNode("David","Infrastructure Head")
    cm=TreeNode("Snowden","Cloud Mangaer")
    am=TreeNode("Bombal","App Manager")
    ah=TreeNode("Amir","Application Head")
    hr=TreeNode("Gels","HR manager")
    rm=TreeNode("Peter","Recrumient Manager")
    pm=TreeNode("Waqas","Policy Manager")
    root.add_child(cto)
    root.add_child(hr)
    cto.add_child(ih)
    cto.add_child(ah)
    ih.add_child(cm)
    ih.add_child(am)
    hr.add_child(rm)
    hr.add_child(pm)
    return root

class Tree(object):
    def __init__(self, data, children=None, parent=None):
        self.data = data
        self.children = children or []
        self.parent = parent
    def add_child(self, data):
        new_child = Tree(data, parent=self)
        self.children.append(new_child)
        return new_child
    def is_root(self):
        return self.parent is None
    def is_leaf(self):
        return not self.children
    def __str__(self):
        if self.is_leaf():
            return str(self.data)
        return '{data} [{children}]'.format(data=self.data, children=', '.join(map(str, self.children)))

# Binary search Tree
class BinarySearchTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add_child(self,data):
        if data==self.data:
           return 
        if data<self.data:
            if self.left:
               self.left.add_child(data)
            else:
                self.left=BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySearchTree(data)
    def in_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.in_order_traversal()
        elements.append(self.data)
        if self.right: 
            elements+=self.right.in_order_traversal()
        return elements
    def post_order(self):
        element=[self.data]
        if self.left:
            element+=self.left.post_order()
        if self.right:
            element+=self.right.post_order()
        return element
    def pre_order(self):
        element=[]
        if self.left:
            element+=self.left.pre_order()
        if self.right:
            element+=self.right.pre_order()
        element.append(self.data)
        return element
    def search(self,value):
        if self.data==value:
            return True
        if value<self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        if value>self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False
    def min(self):
        if self.left:
            return self.left.min()
        return self.data
    def max(self):
        if self.right:
            return self.right.max()
        return self.data
    def is_root(self):
        return 
    def delete(self,value):
        if value<self.data:
            if self.left:
                self.left=self.left.delete(value)
        elif value>self.data:
            if self.right:
                self.right=self.right.delete(value)
        else: 
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            max_val=self.left.max()
            self.data=max_val
            self.left=self.left.delete(max_val)
        return self
    def depth(self):
        if not self.left or not self.right:
            count=0
        if self.left:
            self.left.depth()
        if self.right:
            self.right.depth()
        count+=1
        return count
        
    def cal_sum(self):
        res=0
        if self.left:
            res+=self.left.cal_sum()
        res+=self.data
        if self.right:
            res+=self.right.cal_sum()
        return res            

def build_tree(data):
    root=BinarySearchTree(data[0])
    for i in range(1,len(data)):
        root.add_child(data[i])
    return root
data=[17,4,1,20,9,23,18,34,0]
numbers_tree=build_tree(data) 


# Heaps


# Graphs
class Graphs:
    def __init__(self,edges):
        self.edges=edges
        self.graph_dict={}
        for start,end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]
        print(self.graph_dict)
    def get_path(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return [path]
        if start not in self.graph_dict:
            return []
        res_path=[]
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths=self.get_path(node,end,path)
                for p in new_paths:
                    res_path.append(p)
        return res_path
    def get_sp_path(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return path
        if start not in self.graph_dict:
            return []
        shortest_path=[]
        for node in self.graph_dict[start]:
            if node not in path:
                sp=self.get_sp_path(node,end,path)
                if shortest_path is None or len(sp)<len(shortest_path):
                    shortest_path=sp
        return shortest_path
    
routes=(
    ("Mumbai","Paris"),
    ("Mumbai","Dubai"),
    ("Paris","Dubai"),
    ("Paris","New York"),
    ("Dubai","New York"),
    ("New York","Toronto"),
)
# start="Mumbai"
# end="Paris"
# route_Graph=Graphs(routes)
# print(route_Graph.get_sp_path(start,end))
class Graph:
    def __init__(self,num_nodes,edges):
        self.num_nodes=num_nodes
        self.data=[[] for _ in range(num_nodes)]
        for start,end in edges:
            self.data[start].append(end)
            self.data[end].append(start)
    def __repr__(self):
        return "\n".join("{}:{}".format(n,neighbors)for n,neighbors in enumerate(self.data))
        # res=[[0]*self.num_nodes for _ in range(self.num_nodes)]
        # temp=self.data
        # for i,sublist in enumerate(temp):
        #     for j in sublist:
        #         res[i][j]=1
        # return res
    def __str__(self):
        return self.__repr__()
    def append(self,key,value):
        if key<len(self.data) and value <len(self.data):
            self.data[key].append(value)
            self.data[value].append(key)
    def remove(self,key,value):
        if key<len(self.data) and value<len(self.data):
            if value in self.data[key]:
                self.data[key].remove(value)
            if key in self.data[value]:
                self.data[value].remove(key)
    def bfs(self,root):
        queue=[]
        discoverd=[False]*len(self.data)
        distance=[None]*len(self.data)
        parent=[None]*len(self.data)
        discoverd[root]=True
        distance[root]=0
        queue.append(root)
        idx=0
        while idx < len(queue):
            current=queue[idx]
            idx+=1
            for node in self.data[current]:
                if not discoverd[node]:
                    distance[node]=1+distance[current]
                    parent[node]=current
                    discoverd[node]=True
                    queue.append(node)
        return queue,distance,parent
    def dfs(self,root):
        stack=[]
        discoverd=[False]*len(self.data)
        result=[]
        stack.append(root)
        while len(stack)>0:
            current=stack.pop()
            if not discoverd[current]:
                discoverd[current]=True
                result.append(current)
                for node in self.data[current]:
                    if not discoverd[node]:
                        stack.append(node)
        return result


g1=Graph(5,edges=[(0,1),(0,4),(1,2),(1,4),(1,3),(2,3),(3,4)])
print(g1)






# Quick Sort
def partition(nums,start,end):
    if end is None:
        end=len(nums)-1
    l,r=start,end-1
    pivot=nums[end]
    while r>l:
        if nums[l]<=pivot:
            l+=1
        elif nums[r]>pivot:
            r-=1
        else:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
    if nums[l]>=nums[end]:
        nums[l],nums[end]=nums[end],nums[l]
        return l
    return end
    
def quickSort(nums,start=0,end=None):
    if end is None:
        end=len(nums)-1
    if start < end:
        pivot=partition(nums,start,end)
        quickSort(nums,start,pivot-1)
        quickSort(nums,pivot+1,end)
    return nums

def pascalTriangle(num):
    arr=[]
    i=1
    while i<=num: 
        if len(arr)<=1:
            arr.append([1]*i)
        else:
            arr.append([])
            for j in range(len(arr[i-2])):
                if arr[i-2][j]==1:
                    arr[i-1].append(arr[i-2][j])
                if j+1<=len(arr[i-2])-1:
                    arr[i-1].append(arr[i-2][j]+arr[i-2][j+1])
        i+=1
    return arr
# print(pascalTriangle(num=0))
# Completed (Beats 93%)

def pascalTriangle2(num):
    arr=[]
    i=0
    while i<=num:
        if len(arr)<=1:
            arr.append(1)
        else:
            arr1=[]
            for j in range(len(arr)):
                if arr[j]==1:
                    arr1.append(arr[j])
                if j+1<=len(arr)-1:
                    arr1.append(arr[j]+arr[j+1])
            arr=arr1
        i+=1
    return arr if num<=2 else arr1
# print(pascalTriangle2(num=2))
# Completed (Beats 56%)

def  singleNumber(nums):
    dic={}
    for num in nums:
        if num not in dic:
            dic[num]=1
        else:
            dic[num]+=1
    print(min(dic,key=dic.get))
singleNumber(nums=[1,2,1,2,5])