class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l = []
        n = len(nums)
        i = 0
        while i <= n-1:
            val = [nums[i]]
            while i < n-1 and nums[i+1] == nums[i]+1:
                val.append(nums[i+1])
                i+=1
            l.append(val)
            i+=1
        res = []

        for i in l:
            if len(i) == 1:
                val = str(i[0])
            else:
                val = "->".join([str(i[0]), str(i[-1])])

            res.append(val)

        return res
        

        