class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack stores [index] 
        # pop condition: teperature[i] > temperatures[stack[-1]]
        
        res = [0] * len(temperatures)
        stack =[]
        for i,t in enumerate(temperatures):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                res[j] = i-j
            stack.append(i)
        return res
          

        