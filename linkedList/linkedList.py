class ListNode:
    def __init__(self, value, next=None):
        self.value=value
        self.next=next


def print_list(head):
    p=head
    while p!= None:
       print(p.value)
       p=p.next


def append_element(head,nvalue):
    node=ListNode(nvalue)
    if head==None:# no value in linkedlist
        head=node
    else:
        p=head
        while p.next != None:
            p=p.next
        p.next=node 
    return head 


def get_element(head, index):
    if(index<0):
        print("Enter valid number")
    
    p=head
    i=0
    while i<index and p != None:
        p=p.next
        i += 1
    if p != None:
        print(p.value)

    else:
        print("Error")  


def remove_element(head,v):
    p=head
    q=None
    while p != None and p.value != v:
        q=p
        p=p.ext
    if p==None:
        print("element does not exist")
    else:
        if p==head:
            head=head.next
        else:
            q.next=p.next
    return head                    


#4->1->2
node1=ListNode(4)
node2=ListNode(1)
node3=ListNode(2)
node1.next=node2
node2.next=node3

head=node1

print("Befor")
print_list(head)
append_element(head,5)
print("After")
print_list(head)

print('#####None########')
head=None

print("Befor")
print_list(head)
head=append_element(head,5)
print("After")
print_list(head)

print("getting")
get_element(head, 0)
        
