class Solution:
    def asteroidCollision(self, nums: List[int]) -> List[int]:
        n=len(nums)
        stack=[]
        for i in range(n):
            if nums[i]>0:
                stack.append(nums[i])
            else:
                
               
                while stack and stack[-1]<abs(nums[i]):
                    stack.pop()
                if len(stack)==0:
                    stack.append(nums[i])
                if abs(nums[i])==stack[-1]:
                    stack.pop()            
        return stack
                