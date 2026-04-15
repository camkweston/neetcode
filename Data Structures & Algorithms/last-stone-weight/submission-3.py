import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [s * -1 for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            s1 = heapq.heappop(heap) * -1
            s2 = heapq.heappop(heap) * -1
            to_add = (s1 - s2) * -1

            if to_add != 0:
                heapq.heappush(heap, to_add)
        

        if len(heap) > 0:
            return heap[0] * -1
        else:
            return 0

                
        



        


        