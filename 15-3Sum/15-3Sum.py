# Last updated: 9/20/2025, 5:34:58 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        look_up = {}
        result = []
        n = len(numbers)
        for i in range(0, n):
            look_up[numbers[i]] = i

        print(look_up)

        for i in range(0, n):
            remain = target - numbers[i]
            print(remain)
            if remain in look_up:
                result.append(i+1)
                result.append(look_up[remain]+1)
                return result

        return None