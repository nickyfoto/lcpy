from lcpy import ListNode

def build_head_with_loop(l):
        
        head = ListNode(l.pop(0)) 
        i = 0
        n = head
        loop_node = None
        while l:
            n.next = ListNode(l.pop(0))
            n = n.next
            if i == 1:
                loop_node = n
            i += 1
        n.next = loop_node
        return head
    
def test_detect_loop():
    l = [2,7,5,8,8,8]
    ll = build_head_with_loop(l)
    assert ll.detect_loop() == True