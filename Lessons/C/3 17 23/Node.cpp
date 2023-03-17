//
// Created by fryepre000 on 3/8/2023.
//



struct Node
{
    int data;
    Node* tail;
    Node* head;

    Node(int d,  Node* h, Node* t) : data(d), head(h), tail(t) {}
};