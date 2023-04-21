//
// Created by fryepre000 on 4/21/2023.
//

#include "BTNode.h"

BTNode::BTNode(int v){
    value = v;
    left = nullptr;
    right = nullptr;
}
BTNode::BTNode(int v, BTNode* l, BTNode* r) {
    value = v;
    left = l;
    right = r;
}
BTNode::~BTNode() {
    delete left;
    delete right;
}