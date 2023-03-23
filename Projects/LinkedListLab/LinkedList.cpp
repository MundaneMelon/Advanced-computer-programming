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
    if (search_node->data == value)
    {
        return first_node;
    }
    else
    {
        search_node = search_node->head;
        bool check = false;
        while (true)
        {
            if (search_node->data == value)
            {
                return search_node;
            }
            else if (search_node->head == nullptr)
            {
                std::cout<<"Ummmm yeah it's not here, sorry bout that"<<std::endl;
                return nullptr;
            }
            else
            {
                search_node = search_node->head;
            }
        }
    }

}

void LinkedList::insert(Node to_insert)
{
    to_insert.head = first_node;
    first_node = &to_insert;
}

void LinkedList::printHello()
{
    std::cout<<"hello"<<std::endl;
}
