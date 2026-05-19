class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # change k times of the ch to return the longest string
        # sliding window with pointers to enlarge and reduce
        # Does it have to be contigious?
        l = 0
        res = maxCount = 0 
        hashmap={}
        for r in range(len(s)):           
            hashmap[s[r]] = hashmap.get(s[r],0) +1
            # maintain a legal window 
            maxCount = max(hashmap[s[r]],maxCount)
            while (r-l+1) - maxCount > k:
                hashmap[s[l]]-=1
                l+=1
            res = max(res,r-l+1)
        return res
            

                

        