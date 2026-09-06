class TimeMap:

    def __init__(self):
        self.time_map = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        curr_list = self.time_map.get(key, [])
        curr_list.append((timestamp, value))
        self.time_map[key] = curr_list
        

    def get(self, key: str, timestamp: int) -> str:
        lst = self.time_map[key]
        #find largest timestamp <= timestamp
        
        left = 0
        right = len(lst) - 1
        while left <= right:
            mid = (left + right) // 2
            if lst[mid][0] > timestamp:
                right = mid - 1
            elif lst[mid][0] == timestamp:
                return lst[mid][1]
            else:
                left = mid + 1
        return lst[right][1]
        