class Solution:
    def isPalindrome(self, s: str) -> bool:
        # res=""
        # for c in s:
        #     if c.isalnum():
        #         res+= c.lower()
        s="".join(c.lower() for c in s if c.isalnum())       
        i=0
        j=len(s)-1
        while i<=j:
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True


        
        