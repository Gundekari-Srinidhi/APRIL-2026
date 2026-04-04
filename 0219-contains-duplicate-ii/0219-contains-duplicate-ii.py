class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]].append(i)
            else:
                d[nums[i]]=[i]
        for v in d.values():
            for i in range(len(v)):
                for j in range(i+1,len(v)):
                    if abs(v[i]-v[j])<=k:
                        return True
        return False
            

        