#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

    def __repr__(self):
        return f"Node: {self.data}"

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


def print_singly_linked_list(node):
    while node:
        # fptr.write(str(node.data))
        print("ndoe", node.data)
        node = node.next

        # if node:
        #     fptr.write(sep)


#
# Complete the 'insertNodeAtPosition' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER data
#  3. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

# def insertNodeAtPosition(llist, data, position):
#     node = llist
#     i = 1
#     while node.next:
#         if i == position:
#             new_node = SinglyLinkedListNode(node_data=data)
#             new_node.next = node.next
#             node.next = new_node
#         i += 1
#         node = node.next
#
#     return llist
def reverse(head):
    # prev_node = None
    # node = llist
    # while node.next:
    cur_node = SinglyLinkedListNode(head.data)
    next_node = head.next
    while next_node:
        temp_cur_node = cur_node
        cur_node = SinglyLinkedListNode(next_node.data)
        cur_node.next = temp_cur_node
        next_node = next_node.next
    return cur_node
    # prev_node = None
    # if llist.next:
    #     prev_node = reverse(llist.next)
    # llist.next = None
    # if prev_node is None:
    #     prev_node = llist
    # else:
    #     node = prev_node
    #     while True:
    #         if node.next is None:
    #             node.next = llist
    #             break
    #         node = node.next
    #     # prev_node.next = llist
    # # return prev_node

def deleteNode(llist, position):
    node = llist
    i = 0
    prev_node = None
    while node.next:
        if i == position:
            i
            prev_node.next = node.next
        prev_node = node
        node = node.next
        i += 1

    return llist
def compare_lists(llist1, llist2):
    while llist1 and llist2:
        if llist1.data != llist2.data:
            return 0
        llist1 = llist1.next
        llist2 = llist2.next
        if llist1 is None and llist2 is None:
            return 1
    return 0

def mergeLists(head1, head2, tests_itr):
    print("index: ", tests_itr)
    if head1 and head2:
        if head1.data < head2.data:
            merge_list = head1
            head1 = head1.next
        else:
            merge_list = head2
            head2 = head2.next
    else:
        if tests_itr == 5 and head1.next is None:
            ...
        if head1:
            merge_list = SinglyLinkedListNode(node_data=head1.data)
            head1 = head1.next
        else:
            merge_list = SinglyLinkedListNode(node_data=head2.data)
            head2 = head2.next

    node = merge_list
    while head1 or head2:
        node.next = None
        if head1 and head2:
            if head1.data < head2.data:
                temp_node = SinglyLinkedListNode(node_data=head1.data)
                node.next = temp_node
                head1 = head1.next
            else:
                temp_node = SinglyLinkedListNode(node_data=head2.data)
                node.next = temp_node
                head2 = head2.next
        else:
            if head1:
                temp_node = SinglyLinkedListNode(node_data=head1.data)
                node.next = temp_node
                head1 = head1.next
            elif head2: # is None:
                temp_node = SinglyLinkedListNode(node_data=head2.data)
                node.next = temp_node
                # merge_list.next = head1
                head2 = head2.next
        node = node.next
        # print(node)
    return merge_list


def has_cycle(head):
    node = head
    node_set = set()
    while node:
        node_set.add(node)
        if node in node_set:
            return 1
        node = node.next

        # print("data: ", id(node), hash(node))
        # while new_node:
        #     print(data, new_node.data)
        #     if data == new_node.data:
        #         return 1
        #     new_node = new_node.next

        # if node:
        #     fptr.write(sep)
    return 0


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # llist_count = [2]int(input())
    # llist = SinglyLinkedList()
    # llist2 = SinglyLinkedList()
    # for data in [1, 3, 5, 8]:  # range(llist_count):
    #     # llist_item = int(input())
    #     llist.insert_node(data)
    # for data in []:  # range(llist_count):
    #     # llist_item = int(input())
    #     llist2.insert_node(data)
    # merge_list1 = mergeLists(llist.head, llist2.head)
    # data = 212  # int(input())
    # position = 0 # int(input())
    # print(compare_lists(llist.head, llist2.head))
    # re_head = reverse(llist.head)
    # llist_head = deleteNode(llist.head, position)
    # print("running")
    # print_singly_linked_list(merge_list1)
    # fptr.write('\n')
    #
    # fptr.close()
    lst = []
    for tests_itr in range(1):
        # index = int(input())

        # llist_count = int(input())

        llist = SinglyLinkedList()

        for llist_item in [1, 2, 3]:
            # llist_item = int(input())
            llist.insert_node(llist_item)

        extra = SinglyLinkedListNode(-1);
        temp = llist.head;

        for i in range(3):
            if i == 1:
                extra = temp

            if i != 3 - 1:
                temp = temp.next

        temp.next = extra

        result = has_cycle(llist.head)
        print(result)

    # with open('./merge_data.txt', 'r') as fread:
    #     lst = [int(fline.strip()) for fline in fread]
    # tests = lst.pop(0)
    #
    # for tests_itr in range(tests):
    #     llist1_count = lst.pop(0)
    #
    #     llist1 = SinglyLinkedList()
    #
    #     for _ in range(llist1_count):
    #         llist1_item = lst.pop(0)
    #         llist1.insert_node(llist1_item)
    #
    #     llist2_count = lst.pop(0)
    #
    #     llist2 = SinglyLinkedList()
    #
    #     for _ in range(llist2_count):
    #         llist2_item = lst.pop(0)
    #         llist2.insert_node(llist2_item)
    #
    #     llist3 = mergeLists(llist1.head, llist2.head, tests_itr)
    #
    #     print_singly_linked_list(llist3)

