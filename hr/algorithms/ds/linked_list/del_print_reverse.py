"""
HackerRank  Data Structures  Linked Lists
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      Delete a Node:
      https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem
      Print in Reverse:
      https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem
      Reverse a linked list:
      https://www.hackerrank.com/challenges/reverse-a-linked-list/problem
"""
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


# Delete a Node
def deleteNode(head, position):
    if position == 0:
        return head.next
    
    prev = head
    for _ in range(position-1):
        prev = prev.next
    
    prev.next = prev.next.next
    return head


# Print in Reverse
def reversePrint(head):
    payloads = []
    while head:
        payloads.append(head.data)
        head = head.next
    
    payloads.reverse()
    for payload in payloads:
        print(payload)


# Reverse a linked list
def reverse(head):
    new_head = None
    while head:
        right = head.next
        head.next = new_head
        new_head = head
        head = right
    return new_head
