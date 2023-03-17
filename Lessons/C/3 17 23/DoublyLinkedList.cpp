//
// Created by fryepre000 on 3/17/2023.
//

#include "Node.cpp"
#include "DoublyLinkedList.h"

DoublyLinkedList::DoublyLinkedList(Node* newFirstNode, Node* newLastNode)
{
    first_node = newFirstNode;
    last_node = newLastNode;
}

DoublyLinkedList::~DoublyLinkedList()
{
    first_node = nullptr;
    last_node = nullptr;
}

void DoublyLinkedList::insertAtEnd(int value)
{

    if (!first_node && !last_node) {
        Node* n = new Node(value, nullptr, nullptr);
        first_node = n;
        last_node = n;
    }
    else
    {
        Node* n = new Node(value, nullptr, last_node);
        last_node->head = n;
        last_node = n;
        /*last_node->tail = n;
        last_node = n;*/
    }




    // initialize a new node object
    // if there are no elements yet in the linked list,
    // set the first and last nodes as the new node

    // else,set the new node's tail node as the last node,
    // set the last node's head node as the new node,
    // and set the last node as the new node
}
