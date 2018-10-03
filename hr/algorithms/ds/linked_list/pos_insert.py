"""
HackerRank  Data Structures  Linked Lists   Insert a node at a specific position in a linked list
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem
"""
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node


def print_singly_linked_list(node, sep):
    while node:
        print(str(node.data), end=' ')
        node = node.next


def insertNodeAtPosition(head, data, position):
    node = SinglyLinkedListNode(data)
    if position == 0:
        node.next = head
        return node

    cur = head
    for _ in range(position-1):
        cur = cur.next

    after_node = cur.next
    cur.next = node
    node.next = after_node

    return head


if __name__ == '__main__':
    llist_count = int(input())
    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())
    position = int(input())
    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist.head, ' ')
    print('\n')
