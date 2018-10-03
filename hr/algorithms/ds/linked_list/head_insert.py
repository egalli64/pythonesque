"""
HackerRank  Data Structures  Linked Lists   Insert a node at the head of a linked list
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem
"""
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


def insertNodeAtHead(head, data):
    node = SinglyLinkedListNode(data)
    node.next = head
    return node


if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, ' ')
    print('\n')
