#include "LinkedList.cpp"
#include <iostream>

int main()
{
    LinkedList thing = LinkedList(new Node(1, nullptr));
    thing.insert(2);
    thing.insert(3);
    thing.insert(4);
    thing.insert(5);
    thing.first_node = thing.sort(thing.first_node);
    std::cout<<thing.indexOf(2);



}

