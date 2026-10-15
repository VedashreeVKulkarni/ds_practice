class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        low=0
        high=m-1
        row=-1
        while low<=high:
            mid=(low+high)//2
            if (matrix[mid][0]<=target and target<=matrix[mid][n-1]):
                row=mid
                break
            elif (target<=matrix[mid][0]):
                high=mid-1
            else:
                low=mid+1
        if row==-1:
            return False
        l=0 
        r=n-1
        while l<=r:
            mid =(l+r)//2
            if (matrix[row][mid]==target):
                return True
            elif (matrix[row][mid]>target):
                r=mid-1
            else:
                l=mid+1
        return False        



        