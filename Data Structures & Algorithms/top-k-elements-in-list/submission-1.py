class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCount = {}
        for n in nums:
            freqCount[n] = 1 + freqCount.get(n,0)
        heap = []
        for num in freqCount.keys():
            heapq.heappush(heap, (freqCount[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res