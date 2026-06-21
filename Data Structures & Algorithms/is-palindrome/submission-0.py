class Solution:
    def isPalindrome(self, s: str) -> bool:
        isPali = ''
        for char in s:
            if char.isalnum():
                isPali += char 

        isPali = isPali.lower()

        if isPali == isPali[::-1]:
            return True
        else:
            return False
        
