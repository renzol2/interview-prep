class Solution {
 public:
  vector<int> twoSum(vector<int>& nums, int target) {
    // Map every combination of $target - nums[i]$ to i
    // map[9 - 2] = 1
    map<int, int> m;

    for (int i = 0; i < nums.size(); i++) {
      m[target - nums[i]] = i;
    }

    // Check if map[nums[j]] == some i; return [i, j]
    for (int j = 0; j < nums.size(); j++) {
      // cout << j << endl;
      if (m.find(nums[j]) != m.end()) {
        if (m[nums[j]] == j) continue;
        return {m[nums[j]], j};
      }
    }

    return {-1, -1};
  }
};
