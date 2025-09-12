# Last updated: 9/11/2025, 9:03:11 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        r = []
        for l1 in range(0, n):
            t = target - nums[l1]
            for l2 in range(l1+1, n):
                if t == nums[l2]:
                    return [l1, l2]