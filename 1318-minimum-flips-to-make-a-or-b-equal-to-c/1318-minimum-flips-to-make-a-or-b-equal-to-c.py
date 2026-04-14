class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while a > 0 or b > 0 or c > 0:
            abit = a%2
            bbit = b%2
            cbit = c%2

            if cbit == 1:
                if abit == 0 and  bbit == 0:
                    count+=1
            else:
                if abit == 1 and bbit == 1:
                    count+=2
                elif abit == 1 or bbit == 1:
                    count+=1

            a = a//2
            b = b//2
            c = c//2
        return count
