
<h1>Top Interview 150 Questions Leet Code</h1>

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

# Test case 3: Array with multiple majority elements
nums3 = [2,2,1,1,1,2,2,3,3,3]
print(Solution().majorityElement(nums3)) # Expected output: 2 or 3, depending on the implementation

# Test case 4: Array with no majority element
nums4 = [1,2,3,4,5]
print(Solution().majorityElement(nums4)) # Expected output: 0, as per the implementation
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

<h2>Two Pointers</h2>
<ul>
  <li><b>Valid Palindrome</b></li>
  <li><b>Approach 1</b></li>
  
  ```python
  class Solution:
  
  def isPalindrome(self, s: str) -> bool:
    left, right = 0, len(s) - 1

    # Iterate while left pointer is less than right pointer
    while left < right:
      # Skip non-alphanumeric characters from both sides simultaneously
      while left < right and not (s[left].isalnum()):
        left += 1
      while left < right and not (s[right].isalnum()):
        right -= 1

      # Check if characters at left and right are equal (case-insensitive)
      if left < right:  # Check if pointers haven't crossed yet
        if s[left].lower() != s[right].lower():
          return False
        left += 1
        right -= 1

    return True

  ```
<li><b>Approach 2</b></li>

```python
class Solution:
  """
  This class provides a method to check if a string is a palindrome.
  """
  def isPalindrome(self, s: str) -> bool:
    """
    Checks if a string is a palindrome using two pointers and manual character checks.

    Args:
        s: The string to check.

    Returns:
        True if the string is a palindrome, False otherwise.
    """
    left, right = 0, len(s) - 1

    # Iterate while left pointer is less than or equal to right pointer
    while left <= right:
      # Skip non-alphanumeric characters from the left
      while left < len(s) and not ((ord('a') <= ord(s[left]) <= ord('z')) or (ord('A') <= ord(s[left]) <= ord('Z')) or (ord('0') <= ord(s[left]) <= ord('9'))):
        left += 1
      # Skip non-alphanumeric characters from the right
      while right >= 0 and not ((ord('a') <= ord(s[right]) <= ord('z')) or (ord('A') <= ord(s[right]) <= ord('Z')) or (ord('0') <= ord(s[right]) <= ord('9'))):
        right -= 1

      # Check if characters at left and right are equal (case-insensitive)
      if left <= right:
        # Manual conversion to lowercase for comparison (ASCII)
        if ord('A') <= ord(s[left]) <= ord('Z'):
          leftChar = chr(ord(s[left]) + 32)  # Convert to lowercase (ASCII)
        else:
          leftChar = s[left]
        if ord('A') <= ord(s[right]) <= ord('Z'):
          rightChar = chr(ord(s[right]) + 32)  # Convert to lowercase (ASCII)
        else:
          rightChar = s[right]
        if leftChar != rightChar:
          return False

      # Move pointers inwards
      left += 1
      right -= 1

    return True

```


  <li><b>Is Subsequence</b></li>
  
  ```python
  class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Initialize two pointers at the beginning of s and t
        s_pointer = 0
        t_pointer = 0
        
        # Iterate through t
        while t_pointer < len(t):
            # If the current character in s matches the current character in t, move the pointer in s forward
            if s_pointer < len(s) and s[s_pointer] == t[t_pointer]:
                s_pointer += 1
            # Move the pointer in t forward regardless of whether the characters match
            t_pointer += 1
        
        # If we've gone through all characters in s, it's a subsequence of t
        return s_pointer == len(s)
solution = Solution()

# Example 1
print(solution.isSubsequence("abc", "ahbgdc")) # Output: True

# Example 2
print(solution.isSubsequence("axc", "ahbgdc")) # Output: False


  ```
  <li><b>Two Sum II - Input Array Is Sorted</b></li>
  
  ```python
  class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers at the beginning and end of the array
        left, right = 0, len(numbers) - 1
        
        # Loop until the left pointer is less than the right pointer
        while left < right:
            # Calculate the sum of the numbers at the current positions of the pointers
            current_sum = numbers[left] + numbers[right]
            
            # If the sum is equal to the target, return the indices of the two numbers
            if current_sum == target:
                return [left + 1, right + 1] # Adding 1 to the indices as per the problem statement
            # If the sum is less than the target, move the left pointer one step to the right
            elif current_sum < target:
                left += 1
            # If the sum is greater than the target, move the right pointer one step to the left
            else:
                right -= 1

solution = Solution()

# Example 1
print(solution.twoSum([2,7,11,15], 9)) # Output: [1,2]

# Example 2
print(solution.twoSum([2,3,4], 6)) # Output: [1,3]

# Example 3
print(solution.twoSum([-1,0], -1)) # Output: [1,2]

        
  ```
  
  <li><b>Container With Most Water</b></li>
  
  ```python
  class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize two pointers at the beginning and end of the array
        left, right = 0, len(height) - 1
        # Initialize the maximum area to 0
        max_area = 0
        
        # Loop until the left pointer is less than the right pointer
        while left < right:
            # Calculate the area of the container formed by the two lines at the current positions of the pointers
            current_area = min(height[left], height[right]) * (right - left)
            # Update the maximum area if the current area is greater
            max_area = max(max_area, current_area)
            
            # If the height of the line at the left pointer is less than the height of the line at the right pointer,
            # move the left pointer one step to the right
            if height[left] < height[right]:
                left += 1
            # If the height of the line at the right pointer is less than or equal to the height of the line at the left pointer,
            # move the right pointer one step to the left
            else:
                right -= 1
        
        # Return the maximum area
        return max_area
solution = Solution()

# Example 1
print(solution.maxArea([1,8,6,2,5,4,8,3,7])) # Output: 49

# Example 2
print(solution.maxArea([1,1])) # Output: 1

        
  ```
  <li><b>3Sum</b></li>
  
  ```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the input array
        nums.sort()
        # Initialize the result list
        result = []
        
        # Iterate through the array
        for i in range(len(nums) - 2):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Initialize two pointers for the two-sum problem
            left, right = i + 1, len(nums) - 1
            
            # While the left pointer is less than the right pointer
            while left < right:
                # Calculate the sum of the current number and the numbers at the left and right pointers
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If the sum is 0, add the triplet to the result
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                # If the sum is less than 0, move the left pointer to the right
                elif current_sum < 0:
                    left += 1
                # If the sum is greater than 0, move the right pointer to the left
                else:
                    right -= 1
        
        # Return the result
        return result
solution = Solution()

# Example 1
print(solution.threeSum([-1,0,1,2,-1,-4])) # Output: [[-1,-1,2],[-1,0,1]]

# Example 2
print(solution.threeSum([0,1,1])) # Output: []

# Example 3
print(solution.threeSum([0,0,0])) # Output: [[0,0,0]]

  ```
</ul>

<h2>Sliding Window</h2>
<ul>
  <li>Minimum Size Subarray Sum</li>
  <li>Longest Substring Without Repeating Characters</li>
  <li>Substring with Concatenation of All Words</li>
  <li>Minimum Window Substring</li>
</ul>

<h2>Matrix</h2>
<ul>
  <li>Valid Sudoku</li>
  <li>Spiral Matrix</li>
  <li>Rotate Image</li>
  <li>Set Matrix Zeroes</li>
  <li>Game of Life</li>
</ul>

<h2>Hashmap</h2>
<ul>
  <li>Ransom Note</li>
  <li>Isomorphic Strings</li>
  <li>Word Pattern</li>
  <li>Valid Anagram</li>
  <li>Group Anagrams</li>
  <li>Two Sum</li>
  <li>Happy Number</li>
  <li>Contains Duplicate II</li>
  <li>Longest Consecutive Sequence</li>
</ul>

<h2>Intervals</h2>
<ul>
  <li>Summary Ranges</li>
  <li>Merge Intervals</li>
  <li>Insert Interval</li>
  <li>Minimum Number of Arrows to Burst Balloons</li>
</ul>

<h2>Stack</h2>
<ul>
  <li>Valid Parentheses</li>
  <li>Simplify Path</li>
  <li>Min Stack</li>
  <li>Evaluate Reverse Polish Notation</li>
  <li>Basic Calculator</li>
</ul>

<h2>Linked List</h2>
<ul>
  <li>Linked List Cycle</li>
  <li><b>Add Two Numbers</b></li>
  
  ```python
  class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy head node for the result list
        dummy_head = ListNode(0)
        # Initialize two pointers for the two input lists
        p1, p2 = l1, l2
        # Initialize a pointer for the result list
        p = dummy_head
        # Initialize a carry
        carry = 0
        
        # Iterate through the lists
        while p1 or p2:
            # Calculate the sum of the current digits and the carry
            sum = carry
            if p1:
                sum += p1.val
                p1 = p1.next
            if p2:
                sum += p2.val
                p2 = p2.next
            
            # Update the carry
            carry = sum // 10
            # Create a new node for the current digit
            p.next = ListNode(sum % 10)
            # Move the pointer for the result list
            p = p.next
        
        # If there's still a carry, add a new node with the value of the carry
        if carry > 0:
            p.next = ListNode(carry)
        
        # Return the result list, excluding the dummy head
        return dummy_head.next
solution = Solution()

# Example 1
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
result = solution.addTwoNumbers(l1, l2)
print(result.val, result.next.val, result.next.next.val) # Output: 7 0 8

# Example 2
l1 = ListNode(0)
l2 = ListNode(0)
result = solution.addTwoNumbers(l1, l2)
print(result.val) # Output: 0

# Example 3
l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
result = solution.addTwoNumbers(l1, l2)
print(result.val, result.next.val, result.next.next.val, result.next.next.next.val, result.next.next.next.next.val, result.next.next.next.next.next.val, result.next.next.next.next.next.next.val, result.next.next.next.next.next.next.next.val) # Output: 8 9 9 9 0 0 0 1

        
  ```
  
  <li>Merge Two Sorted Lists</li>
  <li>Copy List with Random Pointer</li>
  <li>Reverse Linked List II</li>
  <li>Reverse Nodes in k-Group</li>
  <li>Remove Nth Node From End of List</li>
  <li>Remove Duplicates from Sorted List II</li>
  <li>Rotate List</li>
  <li>Partition List</li>
  <li>LRU Cache</li>
</ul>

<h2>Binary Tree General</h2>
<ul>
  <li>Maximum Depth of Binary Tree</li>
  <li>Same Tree</li>
  <li>Invert Binary Tree</li>
  <li>Symmetric Tree</li>
  <li>Construct Binary Tree from Preorder and Inorder Traversal</li>
  <li>Construct Binary Tree from Inorder and Postorder Traversal</li>
  <li>Populating Next Right Pointers in Each Node II</li>
  <li>Flatten Binary Tree to Linked List</li>
  <li>Path Sum</li>
  <li>Sum Root to Leaf Numbers</li>
  <li>Binary Tree Maximum Path Sum</li>
  <li>Binary Search Tree Iterator</li>
  <li>Count Complete Tree Nodes</li>
  <li>Lowest Common Ancestor of a Binary Tree</li>
</ul>

<h2>Binary Tree BFS</h2>
<ul>
  <li>Binary Tree Right Side View</li>
  <li>Average of Levels in Binary Tree</li>
  <li>Binary Tree Level Order Traversal</li>
  <li>Binary Tree Zigzag Level Order Traversal</li>
</ul>

<h2>Binary Search Tree</h2>
<ul>
  <li>Minimum Absolute Difference in BST</li>
  <li>Kth Smallest Element in a BST</li>
  <li>Validate Binary Search Tree</li>
</ul>

<h2>Graph General</h2>
<ul>
  <li>Number of Islands</li>
  <li>Surrounded Regions</li>
  <li>Clone Graph</li>
  <li>Evaluate Division</li>
  <li>Course Schedule</li>
  <li>Course Schedule II</li>
</ul>

<h2>Graph BFS</h2>
<ul>
  <li>Snakes and Ladders</li>
  <li>Minimum Genetic Mutation</li>
  <li>Word Ladder</li>
</ul>

<h2>Trie</h2>
<ul>
  <li>Implement Trie (Prefix Tree)</li>
  <li>Design Add and Search Words Data Structure</li>
  <li>Word Search II</li>
</ul>

<h2>Backtracking</h2>
<ul>
  <li>Letter Combinations of a Phone Number</li>
  <li>Combinations</li>
  <li>Permutations</li>
  <li>Combination Sum</li>
  <li>N-Queens II</li>
  <li>Generate Parentheses</li>
  <li>Word Search</li>
</ul>

<h2>Divide & Conquer</h2>
<ul>
  <li>Convert Sorted Array to Binary Search Tree</li>
  <li>Sort List</li>
  <li>Construct Quad Tree</li>
  <li><b>Merge k Sorted Lists</b></li>
  
```python  
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        # Initialize a priority queue (heap) and add the first node of each list to it
        # If a list is empty, it will not be added to the heap
        heap = [(node.val, idx) for idx, node in enumerate(lists) if node]
        heapq.heapify(heap)
        
        # Dummy head for the result linked list
        dummy = ListNode(0)
        current = dummy
        
        while heap:
            # Pop the node with the smallest value from the priority queue
            val, idx = heapq.heappop(heap)
            # Add this node to the result linked list
            current.next = lists[idx]
            current = current.next
            # Move to the next node in the list from which this node was popped
            lists[idx] = lists[idx].next
            # If there are more nodes in the list, add the next node to the heap
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
        
        # Return the result linked list, excluding the dummy head
        return dummy.next
 ```       
</ul>

<h2>Kadane's Algorithm</h2>
<ul>
  <li>Maximum Subarray</li>
  <li>Maximum Sum Circular Subarray</li>
</ul>

<h2>Binary Search</h2>
<ul>
  <li>Search Insert Position</li>
  <li>Search a 2D Matrix</li>
  <li>Find Peak Element</li>
  <li>Search in Rotated Sorted Array</li>
  <li>Find First and Last Position of Element in Sorted Array</li>
  <li>Find Minimum in Rotated Sorted Array</li>
  <li>Median of Two Sorted Arrays</li>
</ul>

<h2>Heap</h2>
<ul>
  <li>Kth Largest Element in an Array</li>
  <li>IPO</li>
  <li>Find K Pairs with Smallest Sums</li>
  <li>Find Median from Data Stream</li>
</ul>

<h2>Bit Manipulation</h2>
<ul>
  <li>Add Binary</li>
  <li>Reverse Bits</li>
  <li>Number of 1 Bits</li>
  <li>Single Number</li>
  <li>Single Number II</li>
  <li>Bitwise AND of Numbers Range</li>
</ul>

<h2>Math</h2>
<ul>
  <li>Palindrome Number</li>
  <li>Plus One</li>
  <li>Factorial Trailing Zeroes</li>
  <li>Sqrt(x)</li>
  <li>Pow(x, n)</li>
  <li>Max Points on a Line</li>
</ul>

<h2>1D DP</h2>
<ul>
  <li>Climbing Stairs</li>
  <li>House Robber</li>
  <li>Word Break</li>
  <li>Coin Change</li>
  <li>Longest Increasing Subsequence</li>
</ul>

<h2>Multidimensional DP</h2>
<ul>
  <li>Triangle</li>
  <li>Minimum Path Sum</li>
  <li>Unique Paths II</li>
  <li>Longest Palindromic Substring</li>
  <li>Interleaving String</li>
  <li>Edit Distance</li>
  <li>Best Time to Buy and Sell Stock III</li>
  <li>Best Time to Buy and Sell Stock IV</li>
  <li>Maximal Square</li>
</ul>

</body>
</html>
