class Solution(object):
    def numRescueBoats(self, people, limit):

        n = len(people)
        count = 0
        people.sort()
        i = 0
        j = n-1

        while i <= j :
            if people[i] + people[j] <= limit :
                count += 1
                i += 1
                j -= 1
            else :
                count += 1
                j -= 1

        return count