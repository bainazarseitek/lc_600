class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]
        for i in range(len(operations)):
            if operations[i]== "D":
                res.append(int(2 * res[-1]))
            elif operations[i]== "C":
                res.pop()
            elif operations[i]== "+":
                prev=res[-2]+res[-1]
                res.append(int(prev))
            else:
                res.append(int(operations[i]))
        return sum(res)
            



        
        