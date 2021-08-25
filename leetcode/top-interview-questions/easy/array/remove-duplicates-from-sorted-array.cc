#include <vector>

class Solution {
public:
  int removeDuplicates(std::vector<int>& nums) {
    if (nums.empty() || nums.size() == 1) return nums.size();
    
    for (size_t i = 1; i < nums.size(); i++) {
      if (nums[i-1] == nums[i]) {
        nums.erase(nums.begin() + i);
        i--;
      }
    }
    
    return nums.size();
  }
};

int main() {
  // put driver code here
  return 0;
}
