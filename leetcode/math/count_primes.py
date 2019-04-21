# """
# 题目：Count the number of prime numbers less than a non-negative number, n.
# Example:
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#
# """


class Solution1:
    """
    这方法好像是太慢了
    """
    def __init__(self):
        self.primes = []

    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        self.primes.append(2)

        for i in range(3, n, 2):
            if self.isPrimes(i):
                self.primes.append(i)
        return len(self.primes)

    def isPrimes(self, n):
        for i in self.primes:
            if n % i == 0:
                return False
        return True

import math

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        
        prime = [1] * n
        prime[0] = prime[1] = 0
        
        for index in range(2, int(math.sqrt(n))+1):
            if prime[index] == 1:
                time = 2
                while index * time < n:
                    prime[index * time] = 0
                    time += 1
                    
        return sum(prime)    

if __name__ == '__main__':
    a = 100000
    solution = Solution1()
    result = solution.countPrimes(a)
    print(result)

# """
# 分析:
# """
