from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #sum(l,r) = prefix[r] - prefix[l]
        #we want sum(l,r) = k
        #prefix[r] - prefix[l] = k
        #looking for prefix[r] to be k + prefix[l]
        # we want previous prefix = curr prefix + k, how many times have we seen that before?
        freq_of_seen_prefix = defaultdict(int)
        freq_of_seen_prefix[0] = 1
        prefixSum = [0] * len(nums)
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            prefixSum[i] = total
        count = 0
        for pre in prefixSum:
            target = pre - k
            count += freq_of_seen_prefix[target]
            freq_of_seen_prefix[pre] += 1
        return count