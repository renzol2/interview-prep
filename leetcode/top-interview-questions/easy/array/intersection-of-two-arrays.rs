use std::collections::HashSet;

impl Solution {
    pub fn intersection(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
       let mut set1 = HashSet::new();
        for n in nums1 {
            set1.insert(n);
        }

        let mut set2 = HashSet::new();

        for n in nums2 {
            if set1.contains(&n) {
                set2.insert(n);
            }
        }

        let v: Vec<i32> = set2.into_iter().collect();
        v
    }
}