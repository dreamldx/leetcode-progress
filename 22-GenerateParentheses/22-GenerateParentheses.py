# Last updated: 4/13/2025, 10:02:17 PM
class Solution:
     def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        answer = []
        def backtracking(input: List[str], l, r) -> List[str]:
          if len(input) == 2*n:
            answer.append("".join(input))

          if l < n:
            input.append("(")
            backtracking(input, l + 1, r)
            input.pop()

          if r < l:
            input.append(")")
            backtracking(input, l, r + 1)
            input.pop()


        backtracking([], 0, 0)
        

        return answer





        