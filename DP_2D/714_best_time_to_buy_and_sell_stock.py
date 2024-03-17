# You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer 
# fee representing a transaction fee. Find the maximum profit you can achieve. You may complete as many 
# transactions as you like, but you need to pay the transaction fee for each transaction.
# Note:
# You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
# The transaction fee is only charged once for each stock purchase and sale.

# Solution: Keep track of the maximum value at each current time period if you own or don't own a stock, then
# loop through the prices list. Next value in the list is entirely dependent on previous max values.
def maxProfit(prices: list[int], fee: int) -> int:
    profit = [[0, 0] for _ in range(len(prices))]
    profit[0] = [-prices[0], 0]

    for i in range(1, len(prices)):
        profit[i][0] = max(profit[i-1][0], profit[i-1][1] - prices[i])
        profit[i][1] = max(profit[i-1][1], profit[i-1][0] + prices[i] - fee)
    
    return profit[len(prices)-1][1]