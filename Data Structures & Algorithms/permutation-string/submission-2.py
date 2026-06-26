class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        window = Counter(s2[:len(s1)])
        l = 0

        for r in range(len(s1), len(s2)):
            if window == s1_count:
                return True
            window[s2[r]] += 1
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]
            l += 1

        return window == s1_count