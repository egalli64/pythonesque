"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 3 - Object-Oriented Programming
 Section 2 - A short journey from procedural to object approach
 10. LAB - Queue aka FIFO: part 2
    Extends the previously developed queue
    isempty() if the queue is empty
"""
import importlib
q = importlib.import_module("3_2_9")


class QueueExt(q.Queue):
    def isempty(self):
        return len(self._data) == 0


queue = QueueExt()
queue.put(1)
queue.put("dog")
queue.put(False)

for i in range(4):
    if not queue.isempty():
        print(queue.get())
    else:
        print("Queue empty")
