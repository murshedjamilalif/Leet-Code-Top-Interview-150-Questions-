
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

  <li>Remove Duplicates from Sorted Array</li>
  <li>Remove Duplicates from Sorted Array II</li>
  <li>Majority Element</li>
  <li>Rotate Array</li>
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
  <li>Valid Palindrome</li>
  <li>Is Subsequence</li>
  <li>Two Sum II - Input Array Is Sorted</li>
  <li>Container With Most Water</li>
  <li>3Sum</li>
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
  <li>Add Two Numbers</li>
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
