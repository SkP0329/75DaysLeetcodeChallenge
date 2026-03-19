class Solution:
    def productExceptSelf(self,nums):
        n=len(nums)
        r=[1]*n
        prefix=1
        for i in range(n):
            r[i]=prefix
            prefix*=nums[i]
        suffix=1
        for i in range(n-1,-1,-1):
            r[i]*=suffix
            suffix*=nums[i]
        return r