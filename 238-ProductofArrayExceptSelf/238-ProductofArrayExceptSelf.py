# Last updated: 9/13/2025, 12:28:02 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero = {}
        total = 1
        n = len(nums)
        r = []
        for i in range(0, n):
            if nums[i] == 0:
                zero[i] = 1
                continue
            total = total * nums[i]

        more_zero = len(zero) > 1
        has_zero = len(zero) > 0
        for i in range(0, n):
            if has_zero and (i in zero):
                if more_zero:
                    r.append(0)
                else:
                    r.append(total)

            if has_zero and (i not in zero):
                r.append(0)
            
            if not has_zero:
                r.append(int(total / nums[i]))

        return r
