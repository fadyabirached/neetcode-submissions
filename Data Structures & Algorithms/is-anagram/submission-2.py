class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lettercounterS = {}
        for char in s:
            if char in lettercounterS:
             lettercounterS[char] += 1
            else:
                lettercounterS[char] = 1
        
        lettercounterT = {}
        for char in t:
            if char in lettercounterT:
                lettercounterT[char] += 1
            else:
                lettercounterT[char] = 1

        if lettercounterS == lettercounterT:
            return True
        else:
            return False
