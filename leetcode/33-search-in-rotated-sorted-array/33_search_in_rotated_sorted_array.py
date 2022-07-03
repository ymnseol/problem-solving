# LeetCode - Search in Rotated Sorted Array(33)
# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def _binary_search(self, nums: List[int], target: int, low: int, high: int) -> int:
        """Find and return the index of the target in the list[low:high+1].

        The given list must be sorted.

        It does NOT guarantee that the returned index is the index 
        of the target appeared first in the given list.

        Args:
            nums (list): The list to find the index of the target.
            target (int): The integer to find the index in the given list.
            low (int): The first index of a subarray to find the target.
            high (int): The last index of a subarray to find the target.

        Returns:
            int: The index of the target found in the given list.
                If the target does not exist in the given list, it returns -1.
        """
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return -1
    
    def _find_tail(self, nums: List[int]) -> int:
        """Find and return the index of the maximum element in the list.

        It works appropriately 
        when the given list is rotated sorted array in ascending order.

        Args:
            nums (list): The list to find the index of the maximum element.
        
        Returns:
            int: The index of the maximum element found in the given list.
                If there is no element, it returns -1.
        """
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if mid + 1 < len(nums):
                if nums[mid] > nums[mid + 1]:
                    return mid
                elif nums[low] <= nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                return mid
        
        return -1
        
    
    def search(self, nums: List[int], target: int) -> int:
        """Find and return the index of the target in the list.

        Args:
            nums (list): The list to find the index of the target.
            target: The element to find its index in the given list.
        
        Returns:
            int: The index of the target found in the given list.
                If the target does not exist in the given list, it returns -1.
        """
        tail = self._find_tail(nums)
        if nums[0] <= target <= nums[tail]:
            return self._binary_search(nums, target, 0, tail)
        else:
            return self._binary_search(nums, target, tail + 1, len(nums) - 1)       
        