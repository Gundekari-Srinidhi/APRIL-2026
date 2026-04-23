class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==-2**31 and divisor==-1:
            return 2**31-1
        sign=0
        if (dividend<0)^(divisor<0):
            sign=-1
        else:
            sign=1
        dividend=abs(dividend)
        divisor=abs(divisor)
        qo=0
        while dividend>=divisor:
            temp=divisor
            multi=1
            while dividend >=(temp<<1):
                temp<<=1
                multi<<=1
            dividend-=temp
            qo+=multi
        return sign*qo
        