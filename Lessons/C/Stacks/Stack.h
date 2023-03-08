class Stack
{
private:
    int *data;
    int top;
public:
    explicit Stack(int size);
    ~Stack();
    void push(int element);
    int pop();
};