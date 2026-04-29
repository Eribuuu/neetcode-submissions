class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_nums = set()
        for num in nums:
            if num in check_nums:
                return True
            else:
                check_nums.add(num)
        return False