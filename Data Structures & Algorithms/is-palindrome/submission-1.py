class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.lower()
        s1 = ''
        for char in s:
            if char.isalnum():
                s1 += char

        left = 0
        right = len(s1)-1
        while left < right:
            if s1[left] == s1[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True
