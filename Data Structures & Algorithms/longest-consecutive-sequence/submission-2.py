class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        result = 1

        if len(nums) == 0:
            return 0
        
        
        for n in nums:
            seen.add(n)
        
        for n in nums:
            if not (n-1) in seen:
                current = n
                longest = 1

                while (current+1) in seen:
                    longest +=1
                    current += 1
                result =max(result, longest)


        return result

        