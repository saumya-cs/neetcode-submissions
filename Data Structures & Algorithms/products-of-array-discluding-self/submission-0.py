class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #current solution works for no zeroes in list

        #edge case 1: there is one zero
        # nums = [-1,0,1,2,3] [0,-6,0,0,0]

        #edge case 2: there are multiple zeroes
        # nums = [0,0,1,2,3]. [0,0,0,0,0]
        total_product = 1
        zero_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            if zero_count == 1 and nums[i] == 0:
                total_product = total_product * 1
            elif (zero_count > 1):
                return [0] * len(nums)
            else:
                total_product = total_product * nums[i]
        returned = nums
        
        for i in range(len(nums)):
            if zero_count == 1:
                if (nums[i] == 0):
                    returned[i] = total_product
                else:
                    returned[i] = 0
            else:
                returned[i] = int(total_product / nums[i])
        
        return returned

        