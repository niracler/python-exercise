# """
# 题目：215. Kth Largest Element in an Array
# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Example 1:
#
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# Example 2:
#
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.
#
# url:https://leetcode.com/problems/kth-largest-element-in-an-array/
# """



import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.min_heap = [-float('inf')] * k
        heapq.heapify(self.min_heap)

        # 构造长度为k的最小堆
        # 要是有比最小堆最上面的大的就弹出最上那个然后放进去, 那么最小堆最上面的那个数就一直是第K大的数
        for num in nums:
            if num > self.min_heap[0]:
                heapq.heappop(self.min_heap)
                heapq.heappush(self.min_heap, num)

        return int(self.min_heap[0])


if __name__ == '__main__':
    k = 3
    arr = [4, 5, 8, 2]
    solution = Solution()
    result = solution.findKthLargest(arr, k)
    print(result)
