class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    if len(prices) <= 1:
      return 0
    
    peaks = []
    valleys = []
    
    # Check first index
    if prices[0] < prices[1]:
      valleys.append(0)
    
    for i in range(1, len(prices)-1):
      # If surrounding prices are higher, current is a valley
      if prices[i] < prices[i+1] and prices[i] <= prices[i-1]:
        valleys.append(i)
      # If surrounding prices are lower, current is peak
      elif prices[i] >= prices[i+1] and prices[i] > prices[i-1]:
        peaks.append(i)
      
    # Check last index
    if prices[len(prices)-1] > prices[len(prices)-2]:
      peaks.append(len(prices)-1)
            
    total_profit = 0
    length = len(peaks) if len(peaks) < len(valleys) else len(valleys)
    for i in range(length):
      total_profit += prices[peaks[i]] - prices[valleys[i]]
    
    return total_profit
