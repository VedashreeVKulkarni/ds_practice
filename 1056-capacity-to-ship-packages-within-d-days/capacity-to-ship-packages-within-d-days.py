class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        ans=high
        while(low<=high):
            mid=(low+high)//2
            curr=0
            d=1
            for w in weights:
              if curr + w >mid:
                d += 1
                curr = 0
              curr += w
            if d<=days:
                    ans=mid
                    high=mid-1
            else:
                    low=mid+1
        return ans                
        