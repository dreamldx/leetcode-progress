# Last updated: 9/19/2025, 6:29:27 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = 0
        q = len(s) - 1
        while p<=q:
            if not s[p].isalnum():
                p += 1
                continue

            if not s[q].isalnum():
                q -= 1
                continue

            if s[p].lower() != s[q].lower():
                return False

            p += 1
            q -= 1

        return True
