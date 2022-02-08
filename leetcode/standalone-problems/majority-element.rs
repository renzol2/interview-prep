use std::collections::HashMap;

impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut m: i32 = 0;
        let mut i: i32 = 0;
        
        for x in nums.iter() {
            if i == 0 {
                m = *x;
                i = 1;
            } else if m == *x {
                i += 1;
            } else {
                i -= 1;
            }
        }
        
        return m;
    }
}
