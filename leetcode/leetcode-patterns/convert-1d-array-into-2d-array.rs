impl Solution {
    pub fn construct2_d_array(original: Vec<i32>, m: i32, n: i32) -> Vec<Vec<i32>> {
        if original.len() as i32 != m * n {
            return Vec::new();
        }

        let mut constructed: Vec<Vec<i32>> = Vec::new();
        let mut index: usize = 0;

        for i in 0..m {
            let mut row = Vec::new();
            for j in 0..n {
                row.push(original[index]);
                index += 1;
            }
            constructed.push(row);
        }

        constructed
    }
}

impl Solution2 {
    pub fn construct2_d_array(original: Vec<i32>, m: i32, n: i32) -> Vec<Vec<i32>> {
        match original.len() as i32 == m * n {
            false => vec![],
            true => original.chunks(n as usize).map(|v| v.to_vec()).collect(),
        }
    }
}
