class Solution:
    def isValid(self, s: str) -> bool:
        # hashmap & stack
        hashmap = {"[":"]","{":"}","(":")"}
        stack =[]
        for c in s:
            if c in hashmap:
                stack.append(c)
            else:
                if not stack or hashmap[stack.pop()] != c:
                    return False
        return len(stack) ==0


        