def removeDuplicates(self,head):
    #Write your code here
    cur=head
    while cur:
        while cur.next and cur.next.data==cur.data:
             cur.next=cur.next.next
        cur=cur.next
    return head
                

