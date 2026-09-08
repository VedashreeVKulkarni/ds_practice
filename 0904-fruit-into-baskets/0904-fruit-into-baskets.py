class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count={}
        l=0
        max_length=0
        for r in range(len(fruits)):
            if fruits[r] in count:
                count[fruits[r]]+=1
            else:
                count[fruits[r]]=1
            while len(count)>2:
                count[fruits[l]]-=1
                if count[fruits[l]]==0:
                    del count[fruits[l]]
                l+=1
            cur_length=r-l+1
            max_length=max(max_length,cur_length)
        return max_length                    