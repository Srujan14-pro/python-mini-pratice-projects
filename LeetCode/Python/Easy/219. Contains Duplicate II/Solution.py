class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dup={}
        for i,num in enumerate(nums):
            if num in dup:
                if i-dup[num]<=k:
                    return True
            dup[num]=i
        return False




       # n=len(nums)

        # # for i in range(n):
        # #     for j in range(i+1,n):
        # #         if nums[i]==nums[j] and abs(i - j) <= k:
        # #             return True
        # # return False
