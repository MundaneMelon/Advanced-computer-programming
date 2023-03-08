//
// Created by fryepre000 on 3/8/2023.
//

#include <iostream>
#include "Node.cpp"

int main() {
    Node* head = nullptr;

    // Add one node at a time
    head = new Node(1, head);
    head = new Node(2, head);
    head = new Node(3, head);
    head = new Node(4,head);

    // Display all nodes
    for (Node* p = head; p; p = p->tail)
    {
        std::cout << p->data << " ";
    }

    // Delete node one at a time
    while (Node* n = head) {
        head = head->tail;
        delete n;
    }
}