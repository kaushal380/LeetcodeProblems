# difficulty: medium
# topics: linked list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:      
    
        dumm = ListNode(0)
        curr = dumm
        curr1 = l1
        curr2 = l2
        carry = 0
        while (curr1 != None) or (curr2 != None) or (carry != 0):
            val1 = 0
            val2 = 0
            if(curr1 != None):
                val1 = curr1.val
            if(curr2 != None):
                val2 = curr2.val

            
            su = val1 + val2 + carry
            print(su)
            print(dumm)
            curr.next = ListNode(su%10)
            carry = su//10
            # curr.next = ListNode(0)
            curr = curr.next
            if(curr1 != None):
                curr1 = curr1.next
            
            if(curr2 != None):
                curr2 = curr2.next
        
        return dumm.next
