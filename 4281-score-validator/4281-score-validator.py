class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        d=deque(events)
        s=c=0

        while d and c!=10:
            cur=d.popleft()
            if cur.isnumeric():
                s+=int(cur)
            elif cur=="W":
                c+=1
            else:
                s+=1


        return [s,c]