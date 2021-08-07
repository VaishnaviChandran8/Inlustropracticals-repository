class Node:
    def __init__(self):
        self.next = 0
        self.next = None
def mergingPoint( head1, head2):
    a = head1
    b = head2
    while (a != b):
        if (a == None) :
            a = head2
        else:
            a = a.next
        if (b == None):
            b = head1
        else:
            b = b.next
        
    return a.data

newnode = None
head1 = Node()
head1.data = 5
head2 = Node()
head2.data = 4
newnode = Node()
newnode.data = 6
head1.next = newnode
newnode = Node()
newnode.data = 7
head1.next.next = newnode
head2.next = newnode
newnode = Node()
newnode.data = 1
head1.next.next.next = newnode
newnode = Node()
newnode.data = 2
head1.next.next.next.next = newnode
head1.next.next.next.next.next = None
print( mergingPoint(head1, head2))
