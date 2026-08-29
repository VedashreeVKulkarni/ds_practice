class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        maximum=0
        for i in seen:
            if i-1 not in seen:
                current=i
                count=1
                while current+1 in seen:
                    current=current+1
                    count+=1
                maximum=max(maximum,count)
        return maximum             
        