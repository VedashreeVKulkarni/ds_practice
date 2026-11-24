class Solution:
    def maxLength(self, nums: List[int]) -> int:
        pro=1
        maxi=0
        for i in range(len(nums)):
            hcf=0
            lcm=1
            for j in range(i,len(nums)):
                hcf=math.gcd(hcf,nums[j])
                lcm=math.lcm(lcm,nums[j]) 
                pro*=nums[j]
                if pro==lcm*hcf:
                    curr=j-i+1
                    maxi=max(curr,maxi)
            pro=1    
        return maxi              
        