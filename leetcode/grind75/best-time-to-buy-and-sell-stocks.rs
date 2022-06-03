impl Solution {
  pub fn max_profit(prices: Vec<i32>) -> i32 {
      let mut profit = 0;
      let mut min_price = 10_000;
      for price in prices {
          if price < min_price {
              min_price = price;
          } else if profit < price - min_price {
              profit = price - min_price;
          }
      }
      profit
  }
}