class ListNode:
    
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self.detect_loop():
            return "linked list has loop in it."
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

    def detect_loop(self):
        
        node = self
        if node is None or node.next is None:
            return False
        slow = node
        fast = node.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
        

    # def __eq__(self, other):
    #     node = self
    #     while node and other:
    #         if node.val != other.val:
    #             return False
    #         node = node.next
    #         other = other.next
    #     return True



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
    


    





















