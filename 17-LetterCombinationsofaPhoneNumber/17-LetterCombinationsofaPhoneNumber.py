# Last updated: 4/2/2025, 8:09:01 PM
import itertools

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []

        map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if len(digits) == 0:
            return []

        ele = []
        for digit in digits:
            letters = map[digit]
            ele.append(letters)

       

        for p in itertools.product(*ele):
            r = ''
            for c in p:
                 r = r + c
            result.append(r)

        return result



