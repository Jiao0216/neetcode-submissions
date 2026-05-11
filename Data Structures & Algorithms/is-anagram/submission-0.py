class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c,0)+1
        for ch in t:
            if ch not in hashmap:
                return False
            hashmap[ch]-=1
            if hashmap[ch]<0:
                return False
        return True


        