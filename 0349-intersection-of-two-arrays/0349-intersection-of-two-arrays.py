class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen=set()
        ans=[]
        for i in range(len(nums1)):
            if nums1[i] not in seen:
                seen.add(nums1[i])
        for j in range(len(nums2)):
            if nums2[j] in seen and nums2[j] not in ans:
                ans.append(nums2[j])
        return ans                
        