class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    # self.printBoard(board)
    # Check rows
    for s in board:
      if not self.isValidSudokuSet(s):
        return False
    
    # Check columns
    boardLen = 9
    col = []
    for i in range(0, boardLen):
      for j in range(0, boardLen):
        col.append(board[j][i])
      if not self.isValidSudokuSet(col):
        return False
      col = []
    
    # Check squares
    numSquares = 3
    squareLen = 3
    for i in range(0, numSquares):
      for j in range(0, numSquares):
        x1, y1 = i * squareLen, j * squareLen
        x2, y2 = (i+1) * squareLen, (j+1) * squareLen
        square = self.getSudokuSquare(board, (x1, y1), (x2, y2))
        # print(square)
        if not self.isValidSudokuSet(square):
          return False
        
    return True

  def isValidSudokuSet(self, sudokuSet: List[str]) -> bool:
    nums = set([str(i) for i in range(1, 10)])
    for s in sudokuSet:
      if s == '.':
        continue
      elif s in nums:
        nums.remove(s)
      elif s not in nums:
        return False
    return True
  
  def getSudokuSquare(self, board: List[List[str]], start: tuple, end: tuple) -> List[str]:
    square = []
    x1, y1 = start
    x2, y2 = end
    for i in range(x1, x2):
      for j in range(y1, y2):
        square.append(board[i][j])
    return square
  
  def printBoard(self, board: List[List[str]]) -> None:
    for row in board:
      print(' '.join(row))
