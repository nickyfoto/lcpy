class ListNode:
    
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        
        l = [self.val]
        n = self
        while n.next:
            l.append(n.next.val)
            n = n.next
        return str(l)

    def reverse(self): 
        prev = None
        current = self 
        while current: 
            next_node = current.next
            current.next = prev 
            prev = current 
            current = next_node
        self = prev 

    def __eq__(self, other):
        node = self
        while node and other:
            if node.val != other.val:
                return False
            node = node.next
            other = other.next
        return True

# l = [2,7,5,8,8,8]

def build_head(l):
    head = l.pop(0)
    head = ListNode(head) 

    n = head
    while l:
        n.next = ListNode(l.pop(0))
        n = n.next
    return head


if __name__ == '__main__':
    pass
    # create a linked list with a cycle in it























