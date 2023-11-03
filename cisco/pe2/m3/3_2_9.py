"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 3 - Object-Oriented Programming
 Section 2 - A short journey from procedural to object approach
 9. LAB Queue aka FIFO
    put(element) - put an element at end of the queue
    get() - take an element from the front of the queue and return it
        or raise a QueueError
"""


class QueueError(IndexError):
    """Exception for Queue"""
    pass


class Queue:
    """My Queue"""

    def __init__(self):
        self._data = []

    def put(self, item):
        self._data.append(item)

    def get(self):
        if len(self._data) > 0:
            item = self._data[0]
            del self._data[0]
            return item
        else:
            raise QueueError


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
