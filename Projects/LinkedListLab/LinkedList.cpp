//
// Created by fryepre000 on 3/21/2023.
//
#include "LinkedList.h"
#include <iostream>

LinkedList::LinkedList()
{
    first_node = nullptr;
}
LinkedList::LinkedList(Node* newFirstNode)
{
    first_node = newFirstNode;
}
LinkedList::~LinkedList()
{
    first_node = nullptr;
}
Node* LinkedList::read(int value)
{
    Node* search_node = first_node;
    while (true)
    {
        if (search_node->data == value)
        {
            return search_node;
        }

        if (search_node->head == nullptr)
        {
            return nullptr;
        }
        search_node = search_node->head;
    }
}

int LinkedList::indexOf(int value)
{
    int index = 0;
    Node* search_node = first_node;
    while(true)
    {
        if (search_node->data == value)
        {
            return index;
        }
        if (search_node->head == nullptr)
        {
            return -1;
        }
        index += 1;
        search_node = search_node->head;
    }
}

void LinkedList::remove(Node* target)
{
    if (first_node == target)
    {
        first_node = target->head;
        delete target;
    }
    else
    {
        Node* search_node = first_node;
        while (true)
        {
            if (search_node->head == target)
            {
                search_node->head = target->head;
                break;
            }
            if (search_node->head == nullptr)
            {
                std::cout<<"Could not find target"<<std::endl;
                break;
            }
            search_node = search_node->head;
        }

    }
}

void LinkedList::insert(int value)
{
    Node* temp = new Node(value, nullptr);
    temp->head = first_node;
    first_node = temp;
}


Node* LinkedList::sort(Node* first_node)
{
    Node* current = first_node;
    Node* sortedFirstNode = NULL;
    while (current != nullptr)
    {
        Node* currentHead = current->head;
        sortedFirstNode = sortedInsert(sortedFirstNode, current);
        current = currentHead;
    }
    return sortedFirstNode;
}

Node* LinkedList::sortedInsert(Node* sortedFirstNode, Node* current)
{
    if (sortedFirstNode == nullptr || sortedFirstNode->data >= current->data)
    {
        current->head = sortedFirstNode;
        return current;
    }
    else
    {
        Node* temp = sortedFirstNode;
        while(temp->head != nullptr && temp->head->data < current->data)
        {
            temp = temp->head;
        }
        current->head = temp->head;
        temp->head = current;
    }
    return sortedFirstNode;
}