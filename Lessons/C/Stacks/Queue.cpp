#include "Queue.h"

Queue::Queue(int size)
{
    data = new int[size];
    top = -1;
    bottom = -1;
};

Queue::~Queue()
{
    delete[] data;
};

void Queue::enqueue(int element)
{
    data[++bottom] = element;
};

int Queue::dequeue()
{
    return data[top++];
};
