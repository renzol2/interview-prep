function maxProfit(prices: number[]): number {
  let min = 10000;
  let profit = 0;
  for (let price of prices) {
    if (price < min) {
      min = price;
    } else if (price - min > profit) {
      profit = price - min;
    }
  }
  return profit;
}
