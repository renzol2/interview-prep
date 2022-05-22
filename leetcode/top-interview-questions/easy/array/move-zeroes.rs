impl Solution {
  pub fn move_zeroes(nums: &mut Vec<i32>) {
      let mut z = Vec::new();
      nums.retain(|x| {
          if *x != 0 { true } else {
              z.push(0);
              false
          }
      });
      nums.append(&mut z);
  }
}