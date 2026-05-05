class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum= []
        previousSum = 0
        for i in range(len(nums)):
            if i == 0:
                prefixSum.append(nums[i])
            else:
                prefixSum.append(prefixSum[i-1] + nums[i])
        for i in range(len(nums)):
            if i == 0:
                if (prefixSum[-1] - prefixSum[i]) == 0:
                    return i
            elif i == len(prefixSum) - 1:
                if (prefixSum [i-1]) == 0:
                    return i
            else:
                if prefixSum[i-1] == (prefixSum[-1] - prefixSum[i]):
                    return i
        return -1
        