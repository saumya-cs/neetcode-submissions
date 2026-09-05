class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freqs = [0] * 3
        for num in nums:
            if num == 0:
                freqs[0] = freqs[0] + 1
            if num == 1:
                freqs[1] = freqs[1] + 1
            if num == 2:
                freqs[2] = freqs[2] + 1

        curr_idx = 0
        for i in range(3):
            freq = freqs[i]
            for j in range(freq):
                nums[curr_idx] = i
                curr_idx += 1
            