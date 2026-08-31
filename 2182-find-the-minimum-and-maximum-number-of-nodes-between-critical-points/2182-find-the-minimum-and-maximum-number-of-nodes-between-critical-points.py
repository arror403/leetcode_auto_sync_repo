class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        
        pos=[]
        for i in range(1, len(arr)-1):
            if (arr[i]>arr[i-1] and arr[i]>arr[i+1]) or (arr[i]<arr[i-1] and arr[i]<arr[i+1]):
                pos.append(i)

        L=len(pos)
        return [-1,-1] if L<2 else [min(pos[i+1]-pos[i] for i in range(L-1)), pos[-1]-pos[0]]