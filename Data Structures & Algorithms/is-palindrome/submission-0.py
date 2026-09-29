class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ""

        for ch in s:
            if ch.isalnum():
                new_s += ch
        left = 0 
        right = len(new_s) - 1
        while left < right:
            if new_s[left] != new_s[right]:
                return False
            
            left += 1
            right -= 1
        return True


        