class Queue
{
private:
    int *data;
    int top;
    int bottom;
public:
    explicit Queue(int size);
    ~Queue();

    void enqueue(int element);
    int dequeue();
};