class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)  # Ensure k is within bounds

        # Step 1: Reverse the entire array
        nums.reverse()

        # Step 2: Reverse the first k elements
        self.reverse(nums, 0, k - 1)

        # Step 3: Reverse the remaining elements
        self.reverse(nums, k, len(nums) - 1)
    
    def reverse(self, arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
