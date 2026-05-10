class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
           
            cur = target - nums[i]
            if cur in hashmap:
                return [hashmap[cur],i]
            hashmap[nums[i]] = i
           
            

        