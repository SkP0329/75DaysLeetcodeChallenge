class Solution:
    def findMaxAverage(self,nums,k):
        s=sum(nums[:k])
        ans=s
        for i in range(k,len(nums)):
            s+=nums[i]-nums[i-k]
            if s>ans:ans=s
        return ans/k