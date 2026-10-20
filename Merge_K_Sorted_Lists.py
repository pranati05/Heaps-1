# Time Complexity : O(NlogK) where N is the no of nodes in each linked list and K is no of linked lists to merge.
# Space Complexity : O(logK)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach
# Using Divide and Conquer Approach. For k lists we partition the lists into half and take first and second list merge them and take 3rd and 4th list merge them at the same level.
# Then merge the merged list of 1 and 2 and merged list of 3 and 4 at the next level.
# After all the lists are merged merge the ouput of 1st and 2nd list with the output of 3rd and 4th list and so on. Finally we will get one merged list.
# Every time we merge k lists, there are log k levels.
# For the first level we merge k/2 lists, then k/4 and so on.
# Second Approach is using minheap to store k nodes in heap and pop the min each time and create a new linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        minheap = []
        for i in range(len(lists)):
            node = lists[i]
            if node:
                heapq.heappush(minheap, (node.val, i, node))
        dummy = ListNode(None)
        head = dummy
        while minheap:
            val, i, node = heapq.heappop(minheap)
            head.next = node
            head = node
            if node.next:
                heapq.heappush(minheap, (node.next.val, i, node.next))
        return dummy.next
#Time - O(NlogK) Where N is the total number of nodes and K is the number of linked lists.
#Space - O(K) 

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        return self.helper(lists, 0, len(lists)-1)
    
    def helper(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.helper(lists, left, mid)
        l2 = self.helper(lists, mid+1, right)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(None)
        currentNode = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                currentNode.next = l1
                l1 = l1.next
            else:
                currentNode.next = l2
                l2 = l2.next
            currentNode = currentNode.next
        if l1:
            currentNode.next = l1
            currentNode = currentNode.next
        if l2:
            currentNode.next = l2
            currentNode = currentNode.next
        return dummy.next
#Time - O(NlogK)
#Space - O(logK)


