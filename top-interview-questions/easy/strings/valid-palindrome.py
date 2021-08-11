class Solution:
  def isPalindrome(self, s: str) -> bool:
    string = self.standardize(s)
    for i in range(len(string) // 2):
      front = i
      back = -1 - i
      if string[front] != string[back]:
        return False
    
    return True
  
  def standardize(self, s: str) -> str:
    alnum = ''
    for c in s:
      if c.isalnum():
        alnum += c
    return alnum.lower()
