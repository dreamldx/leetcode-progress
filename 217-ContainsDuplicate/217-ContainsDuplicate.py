# Last updated: 9/11/2025, 8:48:09 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        d = {}
        for i in range(0, n):
            if nums[i] in d:
              return True
            else:
              d[nums[i]] = 1

        return False