class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        t = ""
        for i in range(0, n *2):
            if i % 2 == 0:
                t = t + s[int(i/2)]
            else:
                t = t + " "
        n=len(t)
        print(t)
        p = 1
        max_p = 0

        r = 0
        r_p = 0
        i = 0
        while True:
            if i >= n:
                break

            if (i + p) >= n or (i - p) < 0:
                # print(f"out of range i->{i}, p->{p}")
                i = i + 1
                p = 1
                continue

            if t[i + p] == t[i - p]:
                if t[i+p] == " " or t[i-p] == " ":
                    # print(f"space skip: i->{i}, p->{p}")
                    p = p + 1
                    continue
                # print(f"i->{i}, p->{p}")
                if p > max_p:
                    max_p = p
                    r = i
                    r_p = p
                p = p + 1
                continue
            else:
                # print(f"no match i->{i}, p->{p}")
                i = i + 1
                p = 0
            

        print(f"r->{r}, r_p->{r_p}")
        
        str = ""
        for i in range(r - r_p, r + r_p + 1):
            if t[i] != " ":
                str = str + t[i]
        return str
        
        