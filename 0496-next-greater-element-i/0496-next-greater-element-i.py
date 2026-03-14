class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        result = []
        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                next_greater[smaller] = num
            stack.append(num)
        for num in nums1:
            result.append(next_greater.get(num, -1))

        return result
