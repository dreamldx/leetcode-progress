# Last updated: 9/11/2025, 9:02:08 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        d = {}
        for i in range(0, n):
          if s[i] in d:
            d[s[i]] = d[s[i]] + 1
          else:
            d[s[i]] = 1

        for i in range(0, m):
          if t[i] not in d:
            return False
          d[t[i]] = d[t[i]] - 1

        print(d)

        for k in d:
          if d[k] != 0:
            return False

        return True