class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        r = []
        for l1 in range(0, n):
            t = target - nums[l1]
            for l2 in range(l1+1, n):
                if t == nums[l2]:
                    return [l1, l2]