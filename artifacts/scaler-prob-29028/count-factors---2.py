# attempt it blind — ask for a coach review when done

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        count = 0
        for i in range (1,int(A**0.5) + 1):
            if (A%i) == 0:
                count += 2 if i * i != A else 1
        return count
            

