class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low=0
        high=n-1
        result=-1
        while low<=high:
            mid=(low+high)//2
            if mid==target:
                return mid
            elif target>mid:
                mid+1
            elif target<mid:
                mid-1
            return mid
        return [-1,-1]

        # first=-1
        # last=-1
        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         if first==-1:
        #             first=i
        #         last=i
        # return[first,last] if first!=-1 else[-1,-1]


