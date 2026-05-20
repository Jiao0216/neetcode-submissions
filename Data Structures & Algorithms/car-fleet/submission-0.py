class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # return how many diff fleet 
        # stack stores how many hours the car needed 
        stack =[]
        car = sorted(zip(position,speed),reverse=True)
        for p,s in car:
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
            


        


        