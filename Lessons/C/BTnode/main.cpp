#include <iostream>
#include "BTNode.h"
#include "BinaryTree.h"

int main() {
    BTNode first = BTNode(25);
    BTNode second = BTNode(13);
    BTNode root = BTNode(15, &first, &second);

}
