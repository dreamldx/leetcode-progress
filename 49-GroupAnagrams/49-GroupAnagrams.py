# Last updated: 9/12/2025, 10:08:06 PM
import copy

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        indics = []
        for s in strs:
          t = "".join(sorted(s))
          if t not in d:
            d[t] = len(d)

          indics.append(d[t])

        result = []
        j = 0
        for i in indics:
          
          if i > (len(result) - 1):
            result.append([])

          result[i].append(strs[j])
          j = j + 1

        return result

