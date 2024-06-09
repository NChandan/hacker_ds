#!/bin/python3

import math
import os
import random
import re
import sys


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


#
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def sortedInsert(llist, data):
    node = llist
    prev_node = None
    new_node = DoublyLinkedListNode(data)
    while node:
        if data < node.data:
            if prev_node is None:
                new_node.next = llist
                llist = new_node
            else:
                prev_node.next = new_node
                new_node.prev = prev_node
                new_node.next = node
                node.prev = new_node
            return llist

        prev_node = node
        node = node.next
    prev_node.next = new_node
    new_node.prev = llist
    return llist
    # Write your code here


if __name__ == '__main__':
    input_data = [1, 3, 1, 2, 4, 5]

    t = input_data.pop(0)

    for t_itr in range(t):
        llist_count = input_data.pop(0)

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = input_data.pop(0)
            llist.insert_node(llist_item)

        data = input_data.pop(0)

        llist1 = sortedInsert(llist.head, data)
