function isValid(s: string): boolean {
  const storage: string[] = [];
  const parentheses = {
    ']': '[',
    '}': '{',
    ')': '(',
  };
  
  for (const c of s) {
    switch (c) {
      case '[':
      case '{':
      case '(':
        storage.push(c);
        break;
      
      case ']':
      case '}':
      case ')':
        if (storage[storage.length - 1] === parentheses[c]) {
          storage.pop(); 
        } else {
          return false;
        }
    }
  }
    
  return storage.length === 0;
};
