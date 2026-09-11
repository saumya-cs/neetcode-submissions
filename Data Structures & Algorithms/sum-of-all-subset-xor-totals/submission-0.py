class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        def backtrack(curr_xor, index):
            if index == len(nums):
                return curr_xor
            #include index
            include_xor = backtrack(curr_xor ^ nums[index], index + 1)
            #exclude index
            exclude_xor = backtrack(curr_xor, index + 1)

            return include_xor + exclude_xor
        return backtrack(0,0)