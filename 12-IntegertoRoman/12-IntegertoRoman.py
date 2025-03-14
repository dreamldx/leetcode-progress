class Solution:
    def leftmost(self, num: int) -> (int, int):
        if num < 0:
            return 0, 0
        highestPower10 = math.floor(math.log10(num))
        return int(num / (10**highestPower10)), int(num % (10**highestPower10))

    def generate_roman(self, n, one: str, five: str, ten: str) -> str:
        if n == 1:
            return one
        elif n == 2:
            return one + one
        elif n == 3:
            return one + one + one
        elif n == 4:
            return one + five
        elif n == 5:
            return five
        elif n == 6:
            return five + one
        elif n == 7:
            return five + one + one
        elif n == 8:
            return five + one + one + one
        elif n == 9:
            return one + ten
        else:
            return ""

    def get_roman(self, n: int, num: int) -> str:
        if num > 1000:
            return self.generate_roman(n, 'M', '', '')
        elif num == 1000:
            return 'M'
        elif num > 100:
            return self.generate_roman(n, 'C', 'D', 'M')
        elif num == 100:
            return 'C'
        elif num > 10:
            return self.generate_roman(n, 'X', 'L', 'C')
        elif num == 10:
            return 'X'
        elif num > 0:
            return self.generate_roman(n, 'I', 'V', 'X')


    def intToRoman(self, num: int) -> str:
        remain = num
        r = ''

        while remain > 0:
            n, m = self.leftmost(remain)
            
            r = r + self.get_roman(n, remain)


            remain = m

        return r

        

        