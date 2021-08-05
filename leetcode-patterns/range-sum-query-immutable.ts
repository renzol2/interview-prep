class NumArray {
  sums: number[];
  constructor(nums: number[]) {
    this.sums = [];

    let tempSum = 0;
    for (const num of nums) {
      tempSum += num;
      this.sums.push(tempSum);
    }
  }

  sumRange(left: number, right: number): number {
    if (left == 0) {
      return this.sums[right];
    }
    return this.sums[right] - this.sums[left - 1];
  }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * var param_1 = obj.sumRange(left,right)
 */
