class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        i=len(digits)-1
        while i>=0:
            if digits[i]<9:
                digits[i]=digits[i]+1
                break
            else:
                digits[i]=0
                i-=1
        if digits[0]==0:
            digits.insert(0,1)
        return digits        
        