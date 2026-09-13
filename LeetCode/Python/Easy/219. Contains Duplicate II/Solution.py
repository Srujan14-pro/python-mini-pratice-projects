class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        for i in range(len(nums)):
            for j in range(i+1,nums):
                if nums[i]==nums[j] and 
        # dup={}
        # for i,num in enumerate(nums):
        #     if num in dup:
        #         if i-dup[num]<=k:
        #             return True
        #     dup[num]=i
        # return False
