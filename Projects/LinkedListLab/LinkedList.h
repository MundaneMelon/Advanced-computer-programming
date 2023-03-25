//
// Created by fryepre000 on 3/21/2023.
//

#ifndef LINKEDLISTLAB_LINKEDLIST_H
#define LINKEDLISTLAB_LINKEDLIST_H
#include "Node.cpp"



class LinkedList
{
private:

public:
    Node* first_node;
    LinkedList();
    LinkedList(Node* newFirstNode);
    ~LinkedList();

    void insert(int value);
    Node* read(int value);
    Node* sort(Node* first_node);
    Node* sortedInsert(Node* sortedFirstNode, Node* current);
    void remove(Node* target);
    int indexOf(int value);

};


#endif //LINKEDLISTLAB_LINKEDLIST_H
