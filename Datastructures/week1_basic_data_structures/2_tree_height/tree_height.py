# python3

import sys
import threading

class Build:
	def __init__(self, value, index):
		self.value = value
		self.parent = index

	def insert(self, value, parent):
		# value that represents head
		if parent == -1:
			parent = None

		self.value = value
		self.parent = parent




def compute_height(n, parents):
	# check if no root height is zero
	if min(parents) != -1:
		return 0

	# argmin of index
    # build tree


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
