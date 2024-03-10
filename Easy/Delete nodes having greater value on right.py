'''Given a singly linked list, remove all the nodes in the list which have any node on their right whose value is greater. (Not just immediate Right , but entire List on the Right)

Example 1:

Input:
LinkedList = 12->15->10->11->5->6->2->3
Output: 15 11 6 3
Explanation: Since, 12, 10, 5 and 2 are
the elements which have greater elements
on the following nodes. So, after deleting
them, the linked list would like be 15,
11, 6, 3.

Example 2:

Input:
LinkedList = 10->20->30->40->50->60
Output: 60
Explanation: All the nodes except the last
node has a greater value node on its right,
so all the nodes except the last node must
be removed.'''

'''
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''
class Solution:
    def reverse(self,head):
        prevnode=None
        curr=head
        
        while curr!=None:
            nextnode=curr.next
            curr.next=prevnode
            prevnode=curr
            curr=nextnode
            
        newhead=prevnode
        
        return newhead
        
    def compute(self,head):
        # 1st reversion
        newhead=self.reverse(head)
        
        # initialization
        max_so_far=newhead.data
        prev=newhead
        curr=newhead.next
        
        # main loop
        while curr!=None:
            next=curr.next
            if curr.data<max_so_far:
                curr=prev
                curr.next=next
            else:
                max_so_far=curr.data
            prev=curr
            curr=next
        
        # 2nd reversion
        head=self.reverse(newhead)
        
        return head 