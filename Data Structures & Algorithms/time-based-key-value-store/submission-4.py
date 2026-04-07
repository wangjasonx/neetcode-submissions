class TimeMap:

    def __init__(self):
        self.time_map = collections.defaultdict(list)
        # key => [(timestamp, value), (timestamp, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append(tuple([timestamp, value]))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        times = self.time_map.get(key, [])

        l, r = 0, len(times) - 1

        while l <= r:
            m = (l + r) // 2

            if times[m][0] <= timestamp:
                res = times[m][1]
                l = m + 1
            else:
                r = m - 1
        
        return res
