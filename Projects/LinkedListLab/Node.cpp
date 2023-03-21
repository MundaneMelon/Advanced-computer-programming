struct Node
{
    int data;
    Node* tail;

    Node(int d, Node* t) : data(d), tail(t) {}
};