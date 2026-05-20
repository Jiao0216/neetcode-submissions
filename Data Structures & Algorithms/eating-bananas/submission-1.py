class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search for k 
        l,r =1,max(piles)
        res=r
        while l <= r:
            mid = (l+r) //2
            total=0
            for p in piles:
                total += (p+mid-1)//mid
            if total <= h:
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res

