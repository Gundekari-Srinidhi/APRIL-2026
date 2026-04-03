class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = []
        for i in nums:
            l.append(abs(i**2))
        return sorted(l)
        