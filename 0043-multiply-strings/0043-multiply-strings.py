class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        sign1=0
        if num1[0]=="-1":
            sign1=-1
        else:
            sign1=1
        ans1=0
        for i in num1:
            digit=ord(i)-ord('0')
            ans1=ans1*10+digit
        ans1=ans1*sign1
        sign2=0
        if num2[0]=="-1":
            sign2=-1
        else:
            sign2=1
        ans2=0
        for i in num2:
            digit=ord(i)-ord('0')
            ans2=ans2*10+digit
        ans2=ans2*sign2
        return str(ans1*ans2)