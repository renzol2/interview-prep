use std::collections::HashMap;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut frequencies: HashMap<i32, u32> = HashMap::new();
        for num in nums {
            match frequencies.get(&num) {
                Some(freq) => {
                    let freq = freq + 1;
                    frequencies.insert(num, freq + 1);
                }
                None => {
                    frequencies.insert(num, 1);
                }
            };
        }

        for (_, frequency) in frequencies {
            if frequency > 1 {
                return true;
            }
        }

        return false;
    }
}