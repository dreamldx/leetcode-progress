# Last updated: 9/13/2025, 12:38:00 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r = [1] * len(nums)
        n = len(nums)

        l = 1
        for i in range(1, n):
          l = l * nums[i-1]
          r[i] = l

        print(r)

        l = 1
        for i in range(n-2, -1, -1):
          print(i)
          l = l * nums[i+1]
          r[i] = r[i] * l

        print(r)
        return r



