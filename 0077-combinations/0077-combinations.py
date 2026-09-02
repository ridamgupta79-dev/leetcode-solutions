class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        result = []

        def comb(a,aset) :
            
            if len(aset) == k :
                result.append(aset.copy())
                return

            for i in range (a, n+1) :
                aset.append(i)
                comb(i+1, aset)
                aset.pop()

        comb(1,[])

        return result


        
