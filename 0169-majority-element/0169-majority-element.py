class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        low=0
        high=len(nums)-1
        mid=(high+low)//2
        return nums[mid]
        