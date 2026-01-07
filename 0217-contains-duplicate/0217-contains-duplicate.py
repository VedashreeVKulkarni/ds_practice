class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums)<2:
         return False
        seen={}
        for num in nums:
            if num in seen:
             return True
            seen[num]=1

        return False
           
