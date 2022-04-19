

def insert(self,head,data): 
#Complete this method
    temp=Node(data)
    if head is None:
        head=temp
        return temp
    current=head
    while current.next is not None:
        current=current.next
    current.next=temp
    return head

