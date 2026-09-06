class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        pre = 1
        for i in range(n):
            pre *= nums[i]
            prefix[i] = pre
        suf = 1
        for i in range(n-1,-1,-1):
            suf *= nums[i]
            suffix[i] = suf
        output = [0] * n
        for i in range(n):
            if i == 0:
                output[i] = suffix[i+1]
            if i == n-1:
                output[i] = prefix[i-1]
            else:
                output[i] = prefix[i-1] * suffix[i+1]
        return output
            