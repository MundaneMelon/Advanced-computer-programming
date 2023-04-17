//
// Created by mikeb on 3/25/2023.
//

#include <cstring>
#include "DataArray.h"

DataArray::DataArray(Node n) {
    Node* temp_n = &n;
    int i = 0;
    while(temp_n) {
        node_array[i] = *temp_n;
        temp_n = temp_n->head;
        i++;
    }
    last = i - 1;
}
DataArray::DataArray() {
    last = 0;
}