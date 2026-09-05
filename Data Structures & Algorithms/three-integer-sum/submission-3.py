class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        seen = set()
        for fixed in range(len(nums)):
            target = -1 * nums[fixed]
            left = fixed + 1
            right = len(nums) - 1
            while (left < right):
                l = nums[left]
                r = nums[right]
                if l + r == target:
                    if (nums[fixed], l, r) not in seen:
                        answer.append([nums[fixed],l,r])
                        seen.add((nums[fixed], l, r))
                    left += 1
                    right -= 1
                elif l + r < target:
                    left += 1
                else:
                    right -= 1
        return answer

        