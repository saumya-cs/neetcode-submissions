class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Recurrence

        maxMoney[i] = max(maxMoney[i-1], maxMoney[i-2] + nums[i])
        """
        if len(nums) == 1:
            return nums[0]
        maxMoney = [0] * len(nums)
        maxMoney[0] = nums[0]
        maxMoney[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            maxMoney[i] = max(maxMoney[i-1], maxMoney[i-2] + nums[i])
        return maxMoney[-1]

        