class Solution:
    def reverse(self, x: int) -> int:
        s = ""
        if str(x)[0] == "-":
            val = "-"
        else:
            val =""
        n = str(abs(x))

        s =n[::-1]
        s = s.lstrip("0")
        
        if s == "":
            return 0
        res = int(val + s)
        if res < -2**31 or res > 2**31 - 1:
            return 0
            
        return res

        