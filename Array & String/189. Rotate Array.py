class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        n = len(nums)
        i = 0
        count = 0
        while count < n:
            pos = (i + k) % len(nums)
            curr = nums[pos]
            nums[pos] = nums[i]
            count += 1
            j = pos
            while j != i and count < n:
                pos = (j + k) % len(nums)
                nums[pos], curr = curr, nums[pos]
                j = pos
                count += 1
            i += 1

# Test case 1: Basic rotation
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
Solution().rotate(nums, k)
print(nums) # Expected output: [5, 6, 7, 1, 2, 3, 4]

# Test case 2: Rotation with k equal to the length of the array
nums = [-1,-100,3,99]
k = 2
Solution().rotate(nums, k)
print(nums) # Expected output: [4, 5, 6, 7, 1, 2, 3]
