class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen={}
        ans=[]
        for i in range(len(nums1)):
            if nums1[i] not in seen:
                seen[nums1[i]]=1
            else:
                seen[nums1[i]]+=1
        for j in range(len(nums2)):
            if nums2[j] in seen and seen[nums2[j]] > 0:
                ans.append(nums2[j])
                seen[nums2[j]]-=1
        return ans

        