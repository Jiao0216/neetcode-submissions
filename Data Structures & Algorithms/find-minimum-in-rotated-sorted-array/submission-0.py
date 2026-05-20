class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search and compare nums[mid] and nums[r] 
        l,r = 0,len(nums)-1
        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l = mid+1
            elif nums[mid] < nums[r]:
                r = mid
        return nums[l]
        

        