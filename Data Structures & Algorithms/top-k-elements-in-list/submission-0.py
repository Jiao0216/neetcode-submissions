class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        bucket = [[] for _ in range(len(nums)+1)]
        for n in nums:
            hashmap[n] = hashmap.get(n,0) +1        
        for num,count in hashmap.items():
            bucket[count].append(num)
        res = []
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res)==k:
                    return res

        



        


        
        