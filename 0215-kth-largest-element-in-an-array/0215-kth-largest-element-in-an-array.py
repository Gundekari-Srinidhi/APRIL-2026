class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def mergesort(nums,l,mid,r):
            res = []
            i = l
            j = mid+1
            while i <= mid and j <= r:
                if nums[i] < nums[j]:
                    res.append(nums[i])
                    i+=1
                else:
                    res.append(nums[j])
                    j+=1
            while i <= mid:
                res.append(nums[i])
                i+=1
            while j <= r:
                res.append(nums[j])
                j+=1
            for x in range(len(res)):
                nums[l+x] = res[x]
            
        def merge(nums,l,r):
            if l<r:
                mid = (l+r)//2
                merge(nums,l,mid)
                merge(nums,mid+1,r)
                mergesort(nums,l,mid,r)

        n = len(nums)   
        merge(nums,0,n-1)
        return nums[-k]
