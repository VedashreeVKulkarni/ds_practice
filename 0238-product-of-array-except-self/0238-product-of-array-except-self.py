class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
     product=[]
     leftpro=1
     for i in range (len(nums)):
        product.append(leftpro)
        leftpro*=nums[i]
     rightpro=1
     for i in range(len(nums) - 1, -1, -1):
        product[i]*=rightpro
        rightpro*=nums[i]
     return product   