class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        # print(self.val)
        l = [self.val]
        n = self
        while n.next:
            l.append(n.next.val)
            n = n.next
        return str(l)


# l = [2,7,5,8,8,8]
def build_head(l):
    head = l.pop(0)
    head = ListNode(head) 

    n = head
    while l:
        n.next = ListNode(l.pop(0))
        n = n.next
    return head
