# Time Complexity : O(NlogK)
# Space Complexity : O(K) space used to store the heap
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach
# Using Min Heap. We iterate through all the N elements in the list so that takes O(N).
# We build the min heap of size K and add K elements to the heap. The adding operation takes O(logK).
# If the heap is greater than k then pop the minimum elements from the heap
# Then return the root element of the heap

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        minheap = []
        for i in range(len(nums)):
            heapq.heappush(minheap, nums[i])
        
        for i in range(len(nums)-k+1):
            value = heapq.heappop(minheap)
        return value
# Time - O(N log K)
# Space - O(N) storing all N elements in the heap

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        minheap = []
        for i in range(len(nums)):
            heapq.heappush(minheap, nums[i])
            if len(minheap) > k:
                heapq.heappop(minheap)
        return minheap[0]
# Time - O(N log K)
# Space - O(K) storing only K elements in the heap

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        maxheap = []
        for i in range(len(nums)):
            heapq.heappush(maxheap, -nums[i])
            if len(maxheap) > len(nums)-k+1:
                heapq.heappop(maxheap)
        return maxheap[0] * (-1)
# Time - O(N log(N−K+1))
# Space - O(N-K) storing only N-K elements in the heap