class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        candidates.sort()

        def answer(index, total, subset) :
            if total == 0 :
                result.append(subset.copy())
                return
            if total < 0 :
                return
            if index >= len(candidates) :
                return

            for i in range (index, len(candidates)) :
                if i>index and candidates[i] == candidates[i-1] :
                    continue

                subset.append(candidates[i])
                sum = total - candidates[i]
                answer(i+1, sum, subset)
                subset.pop()

        answer (0, target, [])
        return result
