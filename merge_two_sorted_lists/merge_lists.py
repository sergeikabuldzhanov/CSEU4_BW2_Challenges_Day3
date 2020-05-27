# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        lst = list()
        lst.append(self.val)
        while self.next:
            self = self.next
            lst.append(self.val)
        return str(lst)
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # get the head of a new list
        if l1.val<l2.val:
            new_head = l1
            l1 = l1.next
        else:
            new_head = l2
            l2 = l2.next

        # make a pointer to the tail of return list
        current = new_head
        # traverse both lists until the end
        while l1 or l2:
            # compare nodes and move appropriate pointers
            if l1 and l2:
                if l1.val<l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
            # if we've reached the end of one list, append it's nodes to return list until end
            elif l1:
                current.next = l1
                l1 = l1.next
            elif l2:
                current.next = l2
                l2 = l2.next
            current = current.next
            
        return new_head
            
lst1 = ListNode(1, ListNode(2, ListNode(9)))
lst2 = ListNode(3, ListNode(5, ListNode(7)))

sumList = Solution().mergeTwoLists(lst1,lst2)

print(sumList)