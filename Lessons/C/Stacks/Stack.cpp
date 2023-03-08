#include "Stack.h"

Stack::Stack(int size)
{
    data = new int[size];
    top = -1;
};

Stack::~Stack()
{
    delete[] data;
};

void Stack::push(int element)
{
    data[++top] = element;
};

int Stack::pop()
{
    return data[top--];
};