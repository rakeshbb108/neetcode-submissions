class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCount = {}
        for n in nums:
            freqCount[n] = 1 + freqCount.get(n,0)
        sort_fre = sorted(freqCount.items(), key = lambda x:x[1])
        res = []
        while len(res) < k:
            res.append(sort_fre.pop()[0])
        return res