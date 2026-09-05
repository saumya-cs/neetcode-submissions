class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        longest = 0
        for i in range(len(nums)):
            if nums[i] - 1 in my_set:
                continue
            count = 1
            amt = 1
            while(nums[i] + amt in my_set):
                count += 1
                amt += 1
            longest = max(longest, count)
        return longest
            

        