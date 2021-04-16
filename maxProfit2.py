# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# Add every small profit
def maxProfit(prices):
        
    prev = float('inf')
    max_profit = 0
    cur_profit = 0
    
    for i, n in enumerate(prices):
    
        if n - prev > 0:
            max_profit += n - prev

        prev = n

    return max_profit

# TODO: What if we want to account for transaction fees instead of buying and selling daily whenever there's a profit?

A = [7,1,5,3,6,4]
B = [1,2,3,4,5]
print(maxProfit(A))