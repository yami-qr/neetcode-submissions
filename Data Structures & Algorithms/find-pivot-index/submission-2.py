class Solution:
    def pivotIndex(self, nums):
        n = len(nums)
        total = sum(nums)
        
        cum = [0] * n
        cum[0] = nums[0]
        
        for i in range(1, n):
            cum[i] = cum[i-1] + nums[i]
        
        for i in range(n):
            if i == 0:
                left = 0
            else:
                left = cum[i-1]
            right = total - cum[i]
            
            if left == right:
                return i
        return -1