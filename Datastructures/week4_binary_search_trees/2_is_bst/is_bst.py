#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(2*10**9) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  
  # Implement correct algorithm here
  return isBstHelper(tree, 0, float("-inf"), float("inf"))

def isBstHelper(tree, idx, min_val, max_val):
  if len(tree) == 0:
    return True

  if idx == -1:
    return True

  # if at leaf node return true
  if tree[idx][1] == -1 and tree[idx][2] == -1:
    #print("current key:{}".format(tree[idx][0]))
    #print("min val: {}".format(min_val))
    #print("max_val: {}".format(max_val))
    #print("check: {}".format(tree[idx][0] < min_val or tree[idx][0] > max_val))
    if tree[idx][0] < min_val or tree[idx][0] >= max_val:
      #print("here")
      #print(" ")
      return False
    #print(" ")
    return True

  # compates to a min value or max_val
  if tree[idx][0] < min_val or tree[idx][0] >= max_val:
    return False

  # traverse left side
  left_check = isBstHelper(tree, tree[idx][1], min_val, tree[idx][0])

  # traverse right side
  right_check = isBstHelper(tree, tree[idx][2], tree[idx][0], max_val)

  return left_check and right_check





def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
