class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seenS = {}
        seenT = {}
        
        for v in s:
            seenS[v] = seenS.get(v, 0) + 1
        for v in t:
            seenT[v] = seenT.get(v, 0) + 1

        for i, v in seenS.items():
            if not i in seenT:
                return False

            if seenT[i] != v:
                return False
        return True
