# Last updated: 9/11/2025, 8:50:20 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      n = len(nums)       
      nums.sort()
      for i in range(1, n):
        if nums[i-1] == nums[i]:
          return True
      return False
      