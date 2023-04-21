cmake_minimum_required(VERSION 3.24)
project(BTnode)

set(CMAKE_CXX_STANDARD 17)

add_executable(BTnode main.cpp BTNode.cpp BTNode.h BinaryTree.cpp BinaryTree.h)
