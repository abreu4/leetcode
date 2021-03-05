# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(prices):
        
        max_profit = 0
        mine = float(inf)
        maxe = 0
        
        for price in prices:
            
            if price < mine: mine = price
            
            else:
                
                new_profit = price - mine
                
                if new_profit > max_profit:
                    max_profit = new_profit
                
        return max_profit