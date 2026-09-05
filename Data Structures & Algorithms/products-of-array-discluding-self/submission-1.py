class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        output = [0]* len(nums)
        zeroes = 0
        for num in nums:
            if num != 0:
                product *= num
            else:
                zeroes += 1
        if zeroes > 1:
            return output
        for i in range(len(nums)):
            if nums[i] == 0:
                output[i] = product
            elif zeroes == 1:
                continue
            else:
                output[i] = int(product / nums[i])
        return output