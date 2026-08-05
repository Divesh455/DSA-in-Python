class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        start = -1
        end = -1

        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                high = mid -1
                start = mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
            
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                end = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return [start,end]