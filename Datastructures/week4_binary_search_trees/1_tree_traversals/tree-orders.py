# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []

    # checks for empty list
    if len(self.key) == 0:
      return self.result

    # start at index root
    self.inOderHelper(0)
    # return result
    return self.result
    
  def inOderHelper(self, idx):
    # traverse left side
    if self.left[idx] != -1:
      self.inOderHelper(self.left[idx])
    # append to the list
    self.result.append(self.key[idx])
    # check right side
    if self.right[idx] != -1:
      self.inOderHelper(self.right[idx])


  def preOrder(self):
    self.result = []
    # Finish the implementation

    # checks for empty list
    if len(self.key) == 0:
      return self.result

    # start at index root
    self.preOderHelper(0)
    # return result
    return self.result
    
  def preOderHelper(self, idx):
    # append to the list
    self.result.append(self.key[idx])
    # traverse left side
    if self.left[idx] != -1:
      self.preOderHelper(self.left[idx])
    # check right side
    if self.right[idx] != -1:
      self.preOderHelper(self.right[idx])

  def postOrder(self):
    self.result = []

    # checks for empty list
    if len(self.key) == 0:
      return self.result
      
    # start at index root
    self.postOderHelper(0)
    # return result
    return self.result
    
  def postOderHelper(self, idx):
    # traverse left side
    if self.left[idx] != -1:
      self.postOderHelper(self.left[idx])
    # check right side
    if self.right[idx] != -1:
      self.postOderHelper(self.right[idx])
    # append to the list
    self.result.append(self.key[idx])


def main():
  # read tree
  tree = TreeOrders()
  tree.read()
  print(" ".join(str(x) for x in tree.inOrder()))
  print(" ".join(str(x) for x in tree.preOrder()))
  print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
