use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }

        let mut freqs: HashMap<char, u32> = HashMap::new();
        for c in s.chars() {
            let counter = freqs.entry(c).or_insert(0);
            *counter += 1;
        }

        for c in t.chars() {
            if freqs.contains_key(&c) {
                let counter = freqs.entry(c).or_insert(0);
                if *counter == 0 { return false; } else { *counter -= 1; }
            } else {
                return false;
            }
        }

        true
    }
}