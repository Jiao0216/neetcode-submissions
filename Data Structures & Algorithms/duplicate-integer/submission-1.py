class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # visit = set()
        # for num in nums:
        #     if num in visit:
        #         return True
        #     visit.add(num)
        # return False
        # Time:O(n).  Space:O(n)
        hashmap={}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
            hashmap[nums[i]] = i
        return False

   