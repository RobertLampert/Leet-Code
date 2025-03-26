class MyQueue(object):

    def __init__(self):
        self.stack = []
        self.stackTemp = []

    def push(self, x):
        while self.stack:
            self.stackTemp.append(self.stack.pop())
        self.stack.append(x)
        while self.stackTemp:
            self.stack.append(self.stackTemp.pop())
        

    def pop(self):
        if self.stack:
            return self.stack.pop()
        """
        :rtype: int
        """
        

    def peek(self):
        if self.stack:
            return self.stack[-1]
        """
        :rtype: int
        """
        

    def empty(self):
        return len(self.stack) == 0
        """
        :rtype: bool
        """
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()