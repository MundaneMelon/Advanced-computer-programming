//
// Created by fryepre000 on 3/21/2023.
//

#ifndef LINKEDLISTLAB_LINKEDLIST_H
#define LINKEDLISTLAB_LINKEDLIST_H
#include "Node.cpp"



class LinkedList
{
private:
    Node* first_node;
    Node* last_node;
public:
    LinkedList();
    LinkedList(Node* newFirstNode, Node* newLastNode);
    ~LinkedList();

    void printHello();
};


#endif //LINKEDLISTLAB_LINKEDLIST_H