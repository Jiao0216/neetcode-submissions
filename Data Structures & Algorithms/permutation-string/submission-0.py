class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # so it doesnt have to be in order
        # two hashmaps to check if they are the same --> True
        # maintain a sliding window (len = len(s1))
        hashmap = {}
        window ={}
        for s in s1:
            hashmap[s] = hashmap.get(s,0) +1
        for r in range(len(s2)):
            window[s2[r]]=window.get(s2[r],0) +1
            
            # when the window is illegal
            if r >= len(s1):
                l = s2[r-len(s1)]
                window[l] -=1
                if window[l]==0:
                    del window[l]

            if hashmap == window:
                return True
        return False


            

        