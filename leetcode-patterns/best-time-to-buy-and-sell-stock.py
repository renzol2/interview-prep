import sys
class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    max_profit = 0
    
    for i in range(0, len(prices) - 1):
      for j in range(i+1, len(prices)):
        profit = prices[j] - prices[i]
        if profit > max_profit:
          max_profit = profit
    
    return max_profit

class Solution2:
  def maxProfit(self, prices: List[int]) -> int:
    min_price = sys.maxsize
    max_profit = 0
    
    for price in prices:
      if price < min_price:
        min_price = price
      elif price - min_price > max_profit:
        max_profit = price - min_price
    
    return max_profit