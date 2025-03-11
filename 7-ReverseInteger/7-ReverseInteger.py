class Solution:
    def reverse(self, x: int) -> int:
        
        result = 0
        t = 0
        sign = -1 if x < 0 else 1
        x = sign * x 
        remain = x
        while remain > 0:
            lowest_digit = remain - int(remain / 10) * 10
            remain = int(remain / 10)
            t = t * 10 + lowest_digit
            print(f"t: {t}")
            if t > 2147483648:
                return 0
            result = t
            print(f"remain: {remain}, result: {result}")
        return sign * result