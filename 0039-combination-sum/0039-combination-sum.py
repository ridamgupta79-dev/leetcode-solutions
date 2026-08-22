class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []

        def solve(index, total, subset) :
            if total == target :
                result.append(subset.copy())
                return
            elif total > target :
                return
            if index >= len(candidates) :
                return

            sum = total + candidates[index]
            subset.append(candidates[index])
            solve(index, sum, subset)

            sum =  total
            subset.pop()
            solve(index+1, sum, subset)

        solve(0, 0, [])

        return result
            
