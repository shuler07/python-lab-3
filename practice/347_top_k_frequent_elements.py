from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count: dict = defaultdict(int)
        for num in nums:
            count[num] += 1
        count = sorted(count.items(), key=lambda x: -x[1])  # type: ignore
        return [count[i][0] for i in range(k)]
