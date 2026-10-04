class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #build prefix and suffix arrays. basically prefix array stores product of elemetns before the elemetn i, and suffix is same as well, just go from the back .
        prefix=[0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                prefix[i]=1
            else:
                prefix[i]=prefix[i-1]*nums[i-1]
        suffix=[0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                suffix[i]=1
            else:
                suffix[i]=suffix[i+1]*nums[i+1]
        #one last pass to get the actual answer array, the previous loops to cache the multiplicative results
        output=[0]*len(nums)
        for i in range(len(nums)):
            output[i]=prefix[i]*suffix[i]
        return output
        