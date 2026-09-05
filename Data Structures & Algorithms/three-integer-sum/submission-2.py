class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = set()
        #left, right pointer values will give you target
        for i in range(len(nums)):
            #-nums[i] = nums[j] + nums[k]
            target = -1 * nums[i]
            left = i + 1
            right = len(nums) - 1
            while(left < right):
                if (nums[left] + nums[right] == target):
                    answer.add((nums[left],nums[right],nums[i]))
                    left += 1
                    right -= 1
                elif (nums[left] + nums[right] > target):
                    right -= 1
                else:
                    left += 1
        return list(answer)