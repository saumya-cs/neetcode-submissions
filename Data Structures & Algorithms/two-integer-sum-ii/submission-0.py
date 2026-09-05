class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #target = 5
        #[1,2,3,4,6,7,8]
        #zero-indexing for actual indexing but must take into account 1 indexing at end
        leftIndex = 0
        rightIndex = len(numbers) - 1

        while (leftIndex < rightIndex): #outer loop can be changed
            matchNum = target - numbers[leftIndex] #what I'm trying to find
            while (numbers[rightIndex] >= matchNum):
                if (numbers[rightIndex] == matchNum):
                    return [leftIndex + 1, rightIndex + 1]
                else:
                    rightIndex -= 1
            leftIndex += 1

#Input: numbers = [1,2,3,4], target = 3

#Output: [1,2]
#matchNum = 2