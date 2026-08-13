class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        left = 0
        result = 0
        basket = {}

        for right in range (0, len(fruits)) :

            if fruits[right] not in basket :
                basket[fruits[right]] = 0
            basket[fruits[right]] += 1

            while len(basket) > 2 :
                basket[fruits[left]] -= 1

                if basket[fruits[left]] == 0 :
                    del basket[fruits[left]]

                left += 1

            result = max(result, right-left+1)

        return result
