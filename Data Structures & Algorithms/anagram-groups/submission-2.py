class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
            
        for word in strs:
            key = {}
            
            for letter in word:
                key[letter] = key.get(letter, 0) + 1
            key = tuple(sorted(key.items()))
            if key not in groups:
                groups[key] = []
            groups[key].append(word)

        return list(groups.values())
                