class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = nums[:]
        pre = 0
        for i in range(len(nums)):
            pre += nums[i]
            prefixSum[i] = pre
        total = 0
        #dictionary: curr[i] - prev[j] = k
        """
        prefixses = [2,1,2,4], k = 2
        seen = {
            2: 1
        }
        """
        seen = {0: 1}
        for i in range(len(prefixSum)):
            target = prefixSum[i] - k
            if target in seen:
                total += seen[target]
            seen[prefixSum[i]] = seen.get(prefixSum[i],0) + 1
            
        return total
            