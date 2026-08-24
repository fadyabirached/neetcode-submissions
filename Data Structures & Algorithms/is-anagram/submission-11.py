class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = {}
        check2 = {}
        for i in range(len(s)):
            if s[i] in check:
                check[s[i]] += 1
            else:
                check[s[i]] = 1
        for i in range(len(t)):
            if t[i] in check2:
                check2[t[i]] += 1
            else:
                check2[t[i]] = 1

        if check == check2:
            return True
        else:
            return False
