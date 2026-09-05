class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        currSum = 0
        minLen = float('inf')
        for right in range(len(nums)):
            currSum += nums[right]
            while currSum >= target:
                minLen = min(minLen, right - left + 1)
                currSum -= nums[left]
                left += 1
        if minLen == float('inf'):
            return 0
        return minLen
                