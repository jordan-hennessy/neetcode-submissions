class TimeMap:

    def __init__(self):
        self.keyStore = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])
                        # e.g. {"alice": [["happy", 1], ["sad", 2]]}
        

    def get(self, key: str, timestamp: int) -> str:

        res = ""

        if key in self.keyStore:
        
            left, right = 0, len(self.keyStore[key])

            while left < right:
                mid = (left + right) // 2

                if self.keyStore[key][mid][1] <= timestamp:
                    left = mid + 1
                    res = self.keyStore[key][mid][0]
                else:
                    right = mid
            
            return res
        else:
            return res


