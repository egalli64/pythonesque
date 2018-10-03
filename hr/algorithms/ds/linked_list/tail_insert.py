"""
HackerRank  Data Structures  Linked Lists   Insert a Node at the Tail of a Linked List
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem
"""
import os


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


def print_singly_linked_list(node, sep):
    while node:
        print(str(node.data), end=' ')
        node = node.next


def printLinkedList(head):
    while head:
        print(head.data)
        head = head.next


def insertNodeAtTail(head, data):
    node = SinglyLinkedListNode(data)
    if not head:
        return node

    tail = head
    while tail.next:
        tail = tail.next

    tail.next = SinglyLinkedListNode(data)
    return head


if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, ' ')
    print('\n')
