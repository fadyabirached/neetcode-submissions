class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent={}
        for i in range(len(nums)):
            if nums[i] in frequent:
                frequent[nums[i]]+= 1
            else:
                frequent[nums[i]] = 1

        key = sorted(frequent.items(), key=lambda x: x[1], reverse=True) 

        result = []
        for item in key[:k]:
            result.append(item[0])

        return result          
