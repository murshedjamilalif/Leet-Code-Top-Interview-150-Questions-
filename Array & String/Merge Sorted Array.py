class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(n)==0:
         return nums1
        else:
         for i in range (m):

           

# Example usage (driver code)
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
solution = Solution()
new_length = solution.merge(nums1, m, nums2, n)

print(f"Modified list: {nums1}")
