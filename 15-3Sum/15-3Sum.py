# Last updated: 4/20/2025, 10:34:24 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        h=len(nums)-1
        if len(nums)==1:
            return 0 if target == nums[0] else -1
        pivot=-1
        while l<=h:
            mid=(l+h)//2
            if mid+1<len(nums) and nums[mid]>nums[mid+1]:
                pivot=mid
                break
            if nums[mid]<nums[0]:
                h=mid-1
            else:
                l=mid+1

        if target<nums[0]:
            l=pivot+1
            h=len(nums)-1
        else:
            l=0
            h=pivot
        if pivot==-1:
            l=0
            h=len(nums)-1

        while l<=h:
            mid=(l+h)//2
            if nums[mid]==target:
                return mid
                break
            if nums[mid]<target:
                l=mid+1
            else:
                h=mid-1
        return -1
