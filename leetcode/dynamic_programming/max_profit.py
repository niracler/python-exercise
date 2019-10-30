# """
# 题目：Best Time to Buy and Sell Stock
#   Go to Discuss
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction
# (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
#
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
#
# """
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 0:
            return 0

        min_to_date = []
        profit_if_sold = []
        diff_from_last = []
        min_to_date.append(prices[0])
        profit_if_sold.append(0)
        diff_from_last.append(0)

        for i in range(1, len(prices)):
            if prices[i] < min_to_date[i - 1]:
                min_to_date.append(prices[i])
            else:
                min_to_date.append(min_to_date[i - 1])
            diff_from_last.append(prices[i] - prices[i - 1])
            profit_if_sold.append(max(0, profit_if_sold[i - 1] + diff_from_last[i]))

        return max(profit_if_sold)


if __name__ == '__main__':
    a = [7, 6, 4, 3, 1]

    solution = Solution()
    result = solution.maxProfit(a)
    print(result)

# """
# 分析:
#
# """
