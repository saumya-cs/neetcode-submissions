class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def recursiveHelper(perm):
            if (len(perm) == len(nums)):
                result.append(perm[:])
                return
            for i in range(len(nums)):
                if (nums[i] in perm):
                    continue
                perm.append(nums[i])
                recursiveHelper(perm)
                perm.pop()
        recursiveHelper([])
        return result
        
        
        