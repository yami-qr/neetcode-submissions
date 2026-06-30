class Solution:
    def isPalindrome(self, s: str) -> bool:
        _s = ""
        for char in s:
            if char.isalnum():
                _s += char.lower()
        return _s == _s[::-1]
        