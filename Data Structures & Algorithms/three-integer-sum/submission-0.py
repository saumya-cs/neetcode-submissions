class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        #-5, -3, 0, 1, 2, 2, 3, 3, 5, 6
        #Are we getting close to 0 with the two together?
        #-nums[i] = nums[j] + nums[k]
       
        returned = list()
        my_set = set()
        for i in range(len(nums)):
            target = -1 * nums[i]
            k = len(nums) - 1
            j = i + 1
            while (j < k):
                if (nums[j] + nums[k] < target):
                    j = j + 1
                elif (nums[j] + nums[k] > target):
                    k = k - 1
                else:
                    triplet = (nums[i],nums[j],nums[k])
                    if triplet not in my_set:
                        returned.append([nums[i],nums[j],nums[k]])
                        my_set.add([nums[i],nums[j],nums[k]])
                    k = k - 1
        return returned



            
