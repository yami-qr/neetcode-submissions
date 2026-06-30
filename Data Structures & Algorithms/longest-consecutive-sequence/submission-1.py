class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        result = 1

        if len(nums) == 0:
            return 0
        
        def setMax(l):
            nonlocal result
            result = max(result, l)
        
        
        for n in nums:
            seen.add(n)
        
        for n in nums:
            longest = 1
            current = n
            
            while (current + 1) in seen:
                longest += 1
                current += 1
            current = n
            
            while (current - 1) in seen:
                longest += 1
                current -= 1
                
            setMax(longest)
        return result

        