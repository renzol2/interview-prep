impl MyStack {
  fn new() -> Self {
      MyStack { stack: vec![] }
  }

  fn push(&mut self, x: i32) {
      self.stack.push(x);
  }

  fn peek(&self) -> i32 {
      self.stack[self.stack.len() - 1]
  }

  fn pop(&mut self) -> i32 {
      self.stack.pop().unwrap()
  }

  fn size(&self) -> usize {
      self.stack.len()
  }

  fn is_empty(&self) -> bool {
      self.stack.len() == 0
  }
}

struct MyQueue {
  main_stack: MyStack,
  transfer_stack: MyStack,
}

/**
* `&self` means the method takes an immutable reference.
* If you need a mutable reference, change it to `&mut self` instead.
*/
impl MyQueue {
  fn new() -> Self {
      MyQueue {
          main_stack: MyStack::new(),
          transfer_stack: MyStack::new(),
      }
  }

  fn push(&mut self, x: i32) {
      // Pop everything from main stack and push into transfer stack
      while !self.main_stack.is_empty() {
          self.transfer_stack.push(self.main_stack.pop());
      }

      // Push x into main stack
      self.main_stack.push(x);

      // Pop everything back from transfer to main stack
      while !self.transfer_stack.is_empty() {
          self.main_stack.push(self.transfer_stack.pop());
      }
  }

  fn pop(&mut self) -> i32 {
      self.main_stack.pop()
  }

  fn peek(&self) -> i32 {
      self.main_stack.peek()
  }

  fn empty(&self) -> bool {
      self.main_stack.is_empty()
  }
}

/**
* Your MyQueue object will be instantiated and called as such:
* let obj = MyQueue::new();
* obj.push(x);
* let ret_2: i32 = obj.pop();
* let ret_3: i32 = obj.peek();
* let ret_4: bool = obj.empty();
*/