class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lowerBound(nums, target):
            low, high = 0, len(nums) - 1
            ans = len(nums)  # first index where nums[i] >= target
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] >= target:
                    ans = mid
                    high = mid - 1   # look left for an earlier one
                else:
                    low = mid + 1    # look right
            return ans

        def upperBound(nums, target):
            low, high = 0, len(nums) - 1
            ans = len(nums)  # first index where nums[i] > target
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] > target:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans

        lb = lowerBound(nums, target)
        if lb == len(nums) or nums[lb] != target:
            return [-1, -1]
        ub = upperBound(nums, target)
        return [lb, ub - 1]