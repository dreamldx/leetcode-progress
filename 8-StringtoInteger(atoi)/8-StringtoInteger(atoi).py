class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)

        leading = True
        sign = 1

        result = 0

        for i in range(0, n):
            if leading:
                if s[i] == ' ':
                   continue
                elif s[i] == '-':
                    sign = -1
                    leading = False
                    continue
                elif s[i] == '+':
                    leading = False
                    continue
                else:
                    leading = False


            if s[i].isdigit():
                result = result * 10 + int(s[i])
                if  sign * result <  -2147483648:
                    result = 2147483648
                    break

                if sign * result >= 2147483648:
                    result = 2147483647
                    break
            else:
                break

        return sign * result


            

             