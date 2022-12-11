# LeetCode - Min Stack(155)
# https://leetcode.com/problems/min-stack

from collections import deque

class MinStack:
    def __init__(self):
        self.stack = []
        self.sorted_list = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.sorted_list:
            self.sorted_list.append(val)
        elif val <= self.sorted_list[-1]:
            self.sorted_list.append(val)
        else:
            self.sorted_list.appendleft(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.sorted_list[-1]:
            self.sorted_list.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.sorted_list[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
