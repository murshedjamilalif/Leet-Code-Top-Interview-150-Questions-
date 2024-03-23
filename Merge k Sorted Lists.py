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