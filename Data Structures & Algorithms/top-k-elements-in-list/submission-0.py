class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #how do we keep track of which element is most frequent?
        #let's say we use a map
        myMap = dict()
        for i in range(len(nums)):
            if nums[i] in myMap:
                myMap[nums[i]] = myMap[nums[i]] + 1
            else:
                myMap[nums[i]]  = 1
        sorted_items = sorted(myMap.items(), key=lambda x: x[1], reverse=True)
        output = []
        for i in range(k):
            output.append((sorted_items[i])[0])
        return output

