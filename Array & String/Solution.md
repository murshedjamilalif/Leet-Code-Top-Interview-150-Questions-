

<h2>Array / String</h2>
<ul>
  <li><b>Merge Sorted Array</b></li>
  
  ```python
  class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m + n - 1
        i = m - 1
        j = n - 1
        
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1
            p -= 1
        
        # If there are still elements left in nums1, they are already in the correct place
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
solution = Solution()
solution.merge(nums1, m, nums2, n)

print(f"Modified list: {nums1}")

  ```
  <li><b>Remove Element</b></li>

```python
class Solution:
    def removeElement(self, nums, val):
        count = 0
        for num in nums:
            if num != val:
                nums[count] = num
                count += 1
        return count

# driver code
nums = [3, 2, 2, 3]
val = 3
solution = Solution()
new_length = solution.removeElement(nums, val)

print(f"Modified list: {nums}")  # Output: Modified list: [2, 2, _, _]
print(f"New length: {new_length}")  # Output: New length: 2
```

  <li><b>Remove Duplicates from Sorted Array</b></li>
  
  ```python
  class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0
        
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1
nums = [1,1,2]
solution = Solution()
k = solution.removeDuplicates(nums)
print(f"Number of unique elements: {k}, nums = {nums[:k]}")

nums = [0,0,1,1,1,2,2,3,3,4]
k = solution.removeDuplicates(nums)
print(f"Number of unique elements: {k}, nums = {nums[:k]}")


  ```
  <li><b>Remove Duplicates from Sorted Array II</b></li>
  
  ```python
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

  ```
  <li>Majority Element</li>
  <li>Approach 1</li>
  
```python

class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        m = {}
        
        for num in nums:
            if num in m:
                m[num] += 1
            else:
                m[num] = 1
        
        n = n // 2
        for key, value in m.items():
            if value > n:
                return key
        
        return 0
# Test case 1: Single element array
nums1 = [3,2,3]
print(Solution().majorityElement(nums1)) # Expected output: 3

# Test case 2: Array with majority element
nums2 = [2,2,1,1,1,2,2]
print(Solution().majorityElement(nums2)) # Expected output: 2

```        

<li>Approach 2</li>

```python
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate  
  ```
  <li><b>Rotate Array</b></li>
  
  ```python
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
  ```
  <li>Best Time to Buy and Sell Stock</li>
  <li>Best Time to Buy and Sell Stock II</li>
  <li>Jump Game</li>
  <li>Jump Game II</li>
  <li>H-Index</li>
  <li>Insert Delete GetRandom O(1)</li>
  <li>Product of Array Except Self</li>
  <li>Gas Station</li>
  <li>Candy</li>
  <li>Trapping Rain Water</li>
  <li>Roman to Integer</li>
  <li>Integer to Roman</li>
  <li>Length of Last Word</li>
  <li>Longest Common Prefix</li>
  <li>Reverse Words in a String</li>
  <li>Zigzag Conversion</li>
  <li>Find the Index of the First Occurrence in a String</li>
  <li>Text Justification</li>
</ul>
