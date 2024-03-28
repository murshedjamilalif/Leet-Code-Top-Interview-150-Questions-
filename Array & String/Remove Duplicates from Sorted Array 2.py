class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 2 # index for placing unique elements (start from 2 to allow for 2 duplicates)
        for num in nums[2:]:
            if num > nums[i-2]: # check against the last unique element
                nums[i] = num
                i += 1
        return i
nums = [1,1,1,2,2,3]
solution = Solution()
k = solution.removeDuplicates(nums)
print(f"Number of unique elements or their second occurrence: {k}, nums = {nums[:k]}")

nums = [0,0,1,1,1,1,2,3,3]
solution = Solution()
k = solution.removeDuplicates(nums)
print(f"Number of unique elements or their second occurrence: {k}, nums = {nums[:k]}")

nums = [1,1]
solution = Solution()
k = solution.removeDuplicates(nums)
print(f"Number of unique elements or their second occurrence: {k}, nums = {nums[:k]}")
