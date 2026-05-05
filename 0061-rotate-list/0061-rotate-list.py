class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head

        m=self.LinkedToArr(head)
        k%=len(m)
        
        return self.ArrToLinked(m[-k:]+m[:-k])
        
        
    def ArrToLinked(self, arr):
        cur=dummy=ListNode()
        for n in arr:
            cur.next=ListNode(n)
            cur=cur.next
        return dummy.next
        
        
    def LinkedToArr(self, head):
        arr=[]
        while head: 
            arr.append(head.val)
            head=head.next
        return arr