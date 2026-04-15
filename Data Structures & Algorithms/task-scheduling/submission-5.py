from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freqs = Counter(tasks)
        heap = []

        for k,v in task_freqs.items():
            heapq.heappush(heap, (-v, k))
        

        cooldown = {}
        result = 0
        popped = []

        while heap:
            popped_rem, popped_id = heapq.heappop(heap)
            popped_rem = -popped_rem

            #print(f"candidate: {popped_id}, {popped_rem}")
            #print(f"popped : {popped}")

            if popped_id in cooldown:
                popped.append((-popped_rem, popped_id))
                
            else:
                popped_rem -= 1
                #print("scheduling ", popped_id, popped_rem)
                print(popped_id)

                if popped_rem > 0:
                    popped.append((-popped_rem, popped_id))
                    cooldown[popped_id] = n + 1
                    
                for rem, task_id in popped:
                    heapq.heappush(heap, (rem, task_id))
                
                popped = []

                cooldown = {k : v - 1 for k,v in cooldown.items() if v > 1}
                print(cooldown)
                result += 1
            
            if len(heap) == 0 and len(popped) > 0:
                print('idle')
                for rem, task_id in popped:
                        heapq.heappush(heap, (rem, task_id))
                
                cooldown = {k : v - 1 for k,v in cooldown.items() if v > 1}
                
                    
                popped = []
                result += 1

        return result



            
        