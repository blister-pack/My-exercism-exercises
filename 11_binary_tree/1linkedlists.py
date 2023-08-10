'''
In linked lists inserting elements is easy and fast because you don't
need to shift elements to make space for a new element or shift
when you want to delete something to close the gap.
Since you just create objects that point at other objects,
a line of order is created     A->B->C->D
If I want to insert T in the line after B, I just need to
make B point at T and make T point at C
'''




class Node:
    def __init__(self, data = None, next = None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beginning(self, data)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

        '''
        what's happening here is that this program runs through
        the list using the next attribute. when there is no next
        it creates a new node in that position
        '''

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        
        return count

    def __repr__(self) -> str:
        if self.head is None:  # usually used to check if an object is None
            return "Linked list is empty"
        

        itr = self.head
        ll_str = ''

        while itr:
            ll_str += str(itr.data) + ' --> '
            itr = itr.next
        return ll_str



if __name__ == '__main__':

    ll = LinkedList()
    ll.insert_at_beginning(4)
    ll.insert_at_beginning(47)
    ll.insert_at_end(666)

    print(ll)

    # stopped yt video at 19:18
