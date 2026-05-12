class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visit = set(nums)
        res = 0
        for n in nums:
            if n-1 not in visit:
                length =0
                while n+length in visit:
                    length +=1
                    res = max(res,length)
        return res
                


            