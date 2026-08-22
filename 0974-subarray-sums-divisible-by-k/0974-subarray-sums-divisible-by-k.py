class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        seen = {0:1}
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            rem = prefix % k
            if rem in seen:
                count += seen[rem]
                seen[rem] += 1
            else:
                seen[rem] = 1
        return count            
        