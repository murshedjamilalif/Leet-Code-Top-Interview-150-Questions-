class Solution:
    def removeElement(self, nums, val) :
        """
        Removes all occurrences of val in nums in-place and returns the new length.

        Args:
            nums: A list of integers.
            val: The value to remove.

        Returns:
            The number of elements in nums that are not equal to val.
        """

        # Count the number of elements that are not val.
        count = 0
        for num in nums:
            if num != val:
                nums[count] = num
                count += 1
        return count
# Example usage (driver code)
nums = [3, 2, 2, 3]
val = 3
solution = Solution()
new_length = solution.removeElement(nums, val)

print(f"Modified list: {nums}")  # Output: Modified list: [2, 2, _, _]
print(f"New length: {new_length}")  # Output: New length: 2