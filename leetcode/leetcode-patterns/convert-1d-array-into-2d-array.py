class Solution:
  def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
    if len(original) != m * n:
      return []

    constructed = []
    index = 0

    for i in range(m):
      row = []
      for j in range(n):
        row.append(original[index])
        index += 1
      constructed.append(row)

    return constructed
