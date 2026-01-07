import math

# You can find the problem here: https://leetcode.com/problems/palindrome-number/


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        stringInt = str(x)
        length = len(stringInt)
        maxIter = math.floor(length / 2)

        for i in range(maxIter):
            if stringInt[i] != stringInt[length - i - 1]:
                return False

        return True

if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(-121))