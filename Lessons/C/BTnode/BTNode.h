//
// Created by fryepre000 on 4/21/2023.
//

#ifndef BTNODE_BTNODE_H
#define BTNODE_BTNODE_H


class BTNode {
private:

public:
    int value;
    BTNode* left;
    BTNode* right;
    explicit BTNode(int v);
    BTNode(int v, BTNode* l, BTNode* r);
    ~BTNode();
};


#endif //BTNODE_BTNODE_H
