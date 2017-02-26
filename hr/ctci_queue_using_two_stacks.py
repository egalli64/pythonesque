"""
HackerRank Tutorials  Cracking the Coding Interview  Queues: A Tale of Two Stacks
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/hackerrank-queues-tale-of-two-stacks.html
      https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks
"""


class MyQueue(object):
    def __init__(self):
        self.head = []
        self.tail = []

    def peek(self):
        self.refill_head()
        return self.head[-1]

    def pop(self):
        self.refill_head()
        return self.head.pop()

    def put(self, value):
        self.tail.append(value)

    def refill_head(self):
        if not self.head:
            while self.tail:
                self.head.append(self.tail.pop())


if __name__ == '__main__':
    queue = MyQueue()
    t = int(input())
    for line in range(t):
        values = map(int, input().split())
        values = list(values)
        if values[0] == 1:
            queue.put(values[1])
        elif values[0] == 2:
            queue.pop()
        else:
            print(queue.peek())
