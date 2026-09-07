class Solution:
    def rob(self, nums: List[int]) -> int:
        #recurrence = max(dp[i-1], dp[i-2] + nums[i])
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        maxMoney1 = [0 for _ in range(len(nums))]
        maxMoney2 = [0 for _ in range(len(nums))]

        maxMoney1[0] = nums[0] #first house
        maxMoney1[1] = max(nums[1], nums[0]) #second house

        maxMoney2[1] = nums[1] #second house
        if len(nums) > 2:
            maxMoney2[2] = max(nums[1], nums[2]) #third house

        for i in range(2, len(nums)-1):
            maxMoney1[i] = max(maxMoney1[i-1], maxMoney1[i-2] + nums[i])

        for i in range(3, len(nums)):
            maxMoney2[i] = max(maxMoney2[i-1], maxMoney2[i-2] + nums[i])
        
        return max(maxMoney1[-2], maxMoney2[-1])
        
