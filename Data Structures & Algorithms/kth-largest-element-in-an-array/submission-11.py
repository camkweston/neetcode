import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for n in nums:
            print(n, heap)
            if len(heap) == k:
                heapq.heappushpop(heap, n)
            else:
                heapq.heappush(heap, n)
        
        print(heap)
        return heap[0]


        