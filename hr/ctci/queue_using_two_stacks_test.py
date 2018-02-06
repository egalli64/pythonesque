"""
HackerRank Tutorials  Cracking the Coding Interview  Queues: A Tale of Two Stacks
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/hackerrank-queues-tale-of-two-stacks.html
      https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks
"""
import unittest

from hr.ctci.queue_using_two_stacks import MyQueue


class TestSolution(unittest.TestCase):
    def test_enqueue(self):
        queue = MyQueue()
        queue.put(42)
        self.assertEqual(42, queue.peek())

    def test_enqueue_2(self):
        queue = MyQueue()
        queue.put(42)
        queue.put(2)
        self.assertEqual(42, queue.peek())

    def test_dequeue(self):
        queue = MyQueue()
        queue.put(42)
        queue.put(2)
        queue.pop()
        self.assertEqual(2, queue.peek())


if __name__ == '__main__':
    unittest.main()
