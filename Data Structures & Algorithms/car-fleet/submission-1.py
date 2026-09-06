class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        myMap = dict()
        for i in range(len(position)):
            myMap[position[i]] = speed[i]
        sortedPositions = sorted(position)
        
        index = len(sortedPositions) - 2
        fleets = 1
        while (index > -1):
            right = sortedPositions[index + 1]
            left = sortedPositions[index]
            while (right <= target):
                if (left == right):
                    fleets -= 1
                right = right + myMap[sortedPositions[index + 1]]
                left = left + myMap[sortedPositions[index]]

            fleets += 1
            index -= 1
        return fleets
