class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack and after calculating push the cur_res back to the stack
        stack =[]
        opp ={"+","-","*","/"}
        for t in tokens:
            if t not in opp:
                stack.append(int(t))
            else:
                a,b = stack.pop(),stack.pop()
                if t == "+":
                    cur = int(a+b)
                    stack.append(cur)
                elif t == "-":
                    cur = int(b-a)
                    stack.append(cur)
                elif t == "*":
                    cur = int(b*a)
                    stack.append(cur)
                elif t == "/" :
                    cur = int(b/a)
                    stack.append(cur)
            
        return stack[0]
        

                    
        
        


        