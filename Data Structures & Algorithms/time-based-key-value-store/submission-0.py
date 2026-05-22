class TimeMap:
    ##. hashmap stores key and value(tuple(timestamp,value))
    ## binary search to track the prev_biggest
    # hashmap = {"alice": (1, "happy")}
 
    def __init__(self):
        self.hashmap ={}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key]=[]
        self.hashmap[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        pairs = self.hashmap[key] ## tuple(timestamp,value)
        l,r = 0,len(pairs) -1
        res=""
        while l <= r:
            mid = (l+r) //2
            if pairs[mid][0] <= timestamp:
                res = pairs[mid][1]
                l = mid+1
            else:
                r = mid-1
        return res





        

        
