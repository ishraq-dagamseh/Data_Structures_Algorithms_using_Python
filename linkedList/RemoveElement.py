class ListNode:
    def __init__(self, value, next=None):
        self.value=value
        self.next=next


def print_list(head):
    p=head
    while p!= None:
       print(p.value)
       p=p.next





def remove_element(head,v):
    p=head
    q=None
    while p != None and p.value != v:
        q=p
        p=p.next
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


print("Befor")
print_list(head)
remove_element(head,2)
print("After")
print_list(head)

        
