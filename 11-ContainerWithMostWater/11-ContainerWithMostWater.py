# Last updated: 10/8/2025, 12:16:29 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        p = 0
        q = n - 1
        m_p = 0
        m_p = n -1
        m = 0
        while p!=q:
          w = q - p
          h = min(height[p], height[q])
          area = w * h

          print(f"{p}-{q} = {area}")

          if area > m:
            m_p = p
            m_q = q
            m = area

          if height[p] < height[q]:
            p = p + 1
          else:
            q = q - 1

        return m

          