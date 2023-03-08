//
// Created by fryepre000 on 3/8/2023.
//

#include "Node.h"

struct Node
{
    int data;
    Node* tail;

    Node(int d, Node* n) : data(d), tail(n) {}
};