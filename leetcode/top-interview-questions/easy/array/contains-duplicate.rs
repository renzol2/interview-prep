use std::collections::HashSet;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut num_set = HashSet::new();
        for num in nums {
            if !num_set.insert(num) {
                return true;
            }
        }

        return false;
    }
} 