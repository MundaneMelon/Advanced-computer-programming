//
// Created by fryepre000 on 3/21/2023.
//
#include "LinkedList.h"
#include <iostream>

LinkedList::LinkedList()
{
    first_node = nullptr;
    last_node = nullptr;
}
LinkedList::LinkedList(Node* newFirstNode, Node* newLastNode)
{
    first_node = newFirstNode;
    last_node = newLastNode;
}
LinkedList::~LinkedList()
{
    first_node = nullptr;
    last_node = nullptr;
}
void LinkedList::printHello()
{
    std::cout<<"hello"<<std::endl;
}
