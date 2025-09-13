# Last updated: 9/12/2025, 10:51:57 PM
from heapq import heappush 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(1) time 
        if k == len(nums):
            return nums
        
        # 1. Build hash map: character and how often it appears
        # O(N) time
        count = Counter(nums)  
        print(count.keys()) 
        # 2-3. Build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get) 
