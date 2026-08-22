class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []
        brackets = [""] * (2 * n)

        def solve(index, total):

            if index >= len(brackets):
                if total == 0:
                    result.append("".join(brackets))
                return

            if total > len(brackets) // 2:
                return

            if total < 0:
                return

            brackets[index] = "("
            sum = total +1
            solve(index + 1, sum)

            brackets[index] = ")"
            sum = total -1
            solve(index + 1, sum)

        solve(0, 0)

        return result

