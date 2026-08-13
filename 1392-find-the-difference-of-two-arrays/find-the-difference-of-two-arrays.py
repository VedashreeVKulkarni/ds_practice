class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1=[]
        ans2=[]
        for i in range(len(nums1)):
            if nums1[i] not in nums2 and nums1[i] not in ans1:
                ans1.append(nums1[i])
        for j in range(len(nums2)):
            if nums2[j] not in nums1 and nums2[j] not in ans2:
                ans2.append(nums2[j])
        return [ans1,ans2]                
        