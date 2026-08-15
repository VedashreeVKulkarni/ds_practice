class Solution:
    def trap(self, height: List[int]) -> int:
        count=0
        max_right=[0]*len(height)
        max_left=[0]*len(height)
        max_left[0] = height[0]
        for i in range(1,len(height)):
            max_left[i]=max(max_left[i-1],height[i])  
        max_right[-1] = height[-1]     
        for j in range(len(height)-2,-1,-1):
            max_right[j]=max(max_right[j+1],height[j])
        minimum=max_left[0]     
        for k in range(len(height)):
            minimum=min(max_left[k],max_right[k])
            count=count+minimum-height[k]
        return count        



        