class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])

        for i in range(m):
            empty = n - 1
            for j in range(n - 1, -1, -1):
                if boxGrid[i][j] == '*':
                    empty = j - 1
                elif boxGrid[i][j] == '#':
                    boxGrid[i][j], boxGrid[i][empty] = boxGrid[i][empty], boxGrid[i][j]
                    empty -= 1

        # rotate
        res = [[None] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][m - 1 - i] = boxGrid[i][j]


        return res

# class Solution:
#     def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
#         m,n=len(boxGrid),len(boxGrid[0])
#         A=[]
        
#         for r in boxGrid:
#             tmp=r
#             for i in range(n-1,-1,-1):
#                 if tmp[i]==".":
#                     t=i
#                     while t:
#                         if tmp[t]=="*": 
#                             break
#                         elif tmp[t]=="#":
#                             tmp[i]="#"
#                             tmp[t]="."
#                             # break
#                         else:
#                             t-=1
                
#             A.append(tmp)

#         print(A)    
        
#         res = [[None] * m for _ in range(n)]
#         for i in range(m):
#             for j in range(n):
#                 res[j][m - 1 - i] = A[i][j]

#         return res