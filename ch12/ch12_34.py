from typing import List
import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            # 리프 노드일때 results에 추가
            if len(elements) == 0:
                results.append(prev_elements[:])
            #순열 생성 재귀 호출
            for e in elements:
                next_elements=elements[:]
                next_elements.remove(e)
                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
        dfs(nums)
        return results
    def permute2(self,nums:List[int])->List[List[int]]:
        return list(itertools.permutations(nums))
print(Solution().permute([2,3,5]))
# [[2, 4, 5], [2, 5, 4], [4, 2, 5], [4, 5, 2], [5, 2, 4], [5, 4, 2]]]
print(Solution().permute2([4,7]))