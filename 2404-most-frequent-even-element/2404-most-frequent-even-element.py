class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        seen={}
        ans=-1
        for num in nums:
            if num not in seen:
                seen[num]=1
            else:
                seen[num]+=1
        for num in seen:
             if num%2==0:
                if ans==-1:
                    ans=num
                elif seen[num]>seen[ans]:
                    ans=num
                elif seen[num]==seen[ans] and num<ans:
                    ans=num
        return ans                
        