//
// Created by fryepre000 on 4/21/2023.
//

#ifndef BTNODE_BINARYTREE_H
#define BTNODE_BINARYTREE_H

#include "BTNode.h"

class BinaryTree {
private:


public:
    BTNode* root;
    BinaryTree(BTNode* r);
    void Insert(int v, BTNode* parent);
    void Insert(int v);
    BTNode* Search(int v, BTNode* r);
};


#endif //BTNODE_BINARYTREE_H
