class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueSet = set(nums)
        best = 0

        for i in uniqueSet:
            if i - 1 not in uniqueSet:
                current = i
                length = 1

                while current + 1 in uniqueSet:
                    current += 1
                    length += 1

                best = max(best, length)

        return best