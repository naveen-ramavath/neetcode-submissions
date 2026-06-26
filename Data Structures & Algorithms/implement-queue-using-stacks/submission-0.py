class MyQueue:

    def __init__(self):
        self.in_stack=[]
        self.out_stack=[]
        

    def push(self, x: int) -> None:
        self.in_stack.append(x)
        

    def pop(self) -> int:
        self.move()
        return self.out_stack.pop()
        

    def peek(self) -> int:
        self.move()
        return self.out_stack[-1]
        

    def empty(self) -> bool:
        self.move()
        return len(self.out_stack)==0


    def move(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        


