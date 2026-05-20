class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time Complexity = O(logn)
        # two pointers and mid pointer to track
        l,r =0, len(nums)-1
        while l <= r:
            m= (l+r)//2
            if nums[m] == target:
                return m
            elif target < nums[m]:
                r = m-1
            else:
                l = m+1
        return -1
            
            

        