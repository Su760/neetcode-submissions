class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            first = heapq.heappop(maxHeap)
            second = heapq.heappop(maxHeap)
            if (first - second) < 0:
                heapq.heappush(maxHeap, first - second)

        if len(maxHeap) == 1:
            return abs(maxHeap[0])
        else:
            return 0