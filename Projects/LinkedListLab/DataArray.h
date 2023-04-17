//
// Created by mikeb on 3/25/2023.
//


#ifndef LINKEDLISTLAB_DATAARRAY_H
#define LINKEDLISTLAB_DATAARRAY_H

#include "Node.cpp"
#include<iostream>

class DataArray {
private:
    Node node_array[3000];
    int last;
    std::string lower(std::string s);
public:
    DataArray();
    explicit DataArray(Node n);
    Node read(int index);
    int indexOf(std::string val);
    void insert(std::string data);
    void remove(std::string val);
    void sort();
};


#endif //LINKEDLISTLAB_DATAARRAY_H
