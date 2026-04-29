class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n
        for i in range(len(arr)):
            rightmax = -1
            for j in range(i+1, len(arr)):
                rightmax = max(rightmax, arr[j])
            ans[i] = rightmax
        return ans
            