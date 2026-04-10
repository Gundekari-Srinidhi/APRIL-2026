class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        si = 0
        do = 0
        for i in nums:
            if i < 10:
                si+=i
            else:
                do+=i
        
        return si != do
        