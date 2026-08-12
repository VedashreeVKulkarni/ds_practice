class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen=set()
        ans=set()
        for i in range(len(nums1)):
            if nums1[i] not in seen:
                seen.add(nums1[i])
        for j in range(len(nums2)):
            if nums2[j] in seen:
                ans.add(nums2[j])
        return list(ans)               
        