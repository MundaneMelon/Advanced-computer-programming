//
// Created by mikeb on 3/25/2023.
//

#include "Node.cpp"

#ifndef LINKEDLISTLAB_DATAARRAY_H
#define LINKEDLISTLAB_DATAARRAY_H


class DataArray {

private:
    Node node_array [3000];
public:
    DataArray(Node* newFirstNode);
    DataArray();
    ~DataArray();
};


#endif //LINKEDLISTLAB_DATAARRAY_H
