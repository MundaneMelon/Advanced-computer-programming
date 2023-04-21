//
// Created by fryepre000 on 4/21/2023.
//

#include "BinaryTree.h"
#include <iostream>

BinaryTree::BinaryTree(BTNode* r) {
    root = r;
};

void BinaryTree::Insert(int v) {
    BTNode* n = root;
    bool check = false;
    while (!check) {
        if (n->left == nullptr and n->right == nullptr) {
            check = true;
            if (v < n->value) {
                n->left = new BTNode(v);
            }
            else if (v >= n->value) {
                n->right = new BTNode(v);
            }
        }
        else if (v < n->value) {
            if (n->left == nullptr) {
                n->left = new BTNode(v);
                check = true;
            }
            else {
                n = root->left;
            }
        }
        else if (v >= n->value) {
            if (n->right == nullptr) {
                n->right = new BTNode(v);
                check = true;
            }
            else {
                n == root->right;
            }
        }
    }

}

void BinaryTree::Insert(int v, BTNode* parent) {

}

BTNode* BinaryTree::Search(int v, BTNode* r) {
    if (v == r->value) {
        return r;
    }
    else if (v < r->value && r->left != nullptr) {
        target = Search(v, r->left);
    }
}