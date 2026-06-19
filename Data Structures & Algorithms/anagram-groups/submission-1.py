class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for i in range(len(strs)):
            counter = {}
            for char in strs[i]:
                if char in counter:
                    counter[char] += 1
                else:
                    counter[char] = 1

            key = tuple(sorted(counter.items())) 

            if key not in groups:
                groups[key] = []          
            groups[key].append(strs[i])  

        return list(groups.values()) 