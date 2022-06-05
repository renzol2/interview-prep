class MyStack {
  stack: Array<number>;
  
  constructor() {
      this.stack = [];
  }
  
  push(x: number): void {
      this.stack.push(x);
  }

  peek(): number {
      return this.stack[this.stack.length - 1];
  }

  pop(): number {
      return this.stack.pop();
  }

  size(): number {
      return this.stack.length;
  }

  isEmpty(): boolean {
      return this.stack.length === 0;
  }
}

// input: [1, 2, 3, 4, 5]
// push input in, pop input out
// stack always pop out of back
// top of stack is on the right
// stack1: [4, 3, 2, 1]
// stack2: []


class MyQueue {
  stack1: MyStack;
  stack2: MyStack;

  constructor() {
      this.stack1 = new MyStack();
      this.stack2 = new MyStack();
  }

  push(x: number): void {
      // pop everything into stack 2
      while (!this.stack1.isEmpty()) {
          this.stack2.push(this.stack1.pop());
      }
      
      // put new number into stack 1
      this.stack1.push(x);

      // pop everything back from stack 2 into stack 1
      while (!this.stack2.isEmpty()) {
          this.stack1.push(this.stack2.pop());
      }
  }

  pop(): number {
      return this.stack1.pop();
  }

  peek(): number {
      return this.stack1.peek();
  }

  empty(): boolean {
      return this.stack1.isEmpty();
  }
}

/**
* Your MyQueue object will be instantiated and called as such:
* var obj = new MyQueue()
* obj.push(x)
* var param_2 = obj.pop()
* var param_3 = obj.peek()
* var param_4 = obj.empty()
*/