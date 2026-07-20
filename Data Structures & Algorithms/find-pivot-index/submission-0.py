class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        def sumBeforeN(n):
            res = 0
            for i in range(n):
                res += nums[i]
            return res

        def sumAfterN(n):
            res = 0
            for i in range(n+1, len(nums)):
                res += nums[i]
            return res
        
        def equal(n):
            #print("BEFORE :", sumBeforeN(n), "AFTER : ", sumAfterN(n))
            return sumBeforeN(n) == sumAfterN(n)
        
        for i in range(len(nums)):
            if equal(i):
                return i
        
        return -1
                