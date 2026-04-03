class Solution
{
public int maximumCount(int[] nums)
{
int n=nums.length;
int l=0,r=n-1;
while(l<=r)
{
int m=(l+r)/2;
if(nums[m]<0)
l=m+1;
else 
r=m-1;
}
int neg=l;
l=0;r=n-1;
while(l<=r)
{
int m=(l+r)/2;
if(nums[m]<=0)
l=m+1;
else
r=m-1;
}
int pos=n-l;
return Math.max(neg,pos);
}
}