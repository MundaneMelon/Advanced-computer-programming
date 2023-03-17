//
// Implement Queues as doubly linked list
//

#include "Node.cpp"

class DoublyLinkedList {
private:
    Node* first_node;
    Node* last_node;

public:
    DoublyLinkedList(Node* firstNode,Node* lastNode);
    ~DoublyLinkedList();

    void insertAtEnd(int);
    Node* remove_from_front();

};
