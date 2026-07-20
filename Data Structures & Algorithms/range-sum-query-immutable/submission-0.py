class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        cum = [0] * n
        cum[0] = nums[0]

        for i in range(1, n):
            cum[i] = cum[i-1] + nums[i]
        self.cum = cum
        
        

    def sumRange(self, left: int, right: int) -> int:
        if (left-1) < 0:
            return self.cum[right]
        return self.cum[right] - self.cum[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)