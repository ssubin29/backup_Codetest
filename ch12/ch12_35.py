from typing import List
import itertools

class Solution:
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(elements[:])
                return
            # 자신 이전의 모든 값을 고정하여 재귀 호출
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()
        dfs([], 1, k)
        return results

    def combine2(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n + 1), k))

print(Solution().combine2(5,4))
# [(1, 2, 3, 4), (1, 2, 3, 5), (1, 2, 4, 5), (1, 3, 4, 5), (2, 3, 4, 5)]