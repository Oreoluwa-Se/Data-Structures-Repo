# python3


class MinHeap:
    def __init__(self, array):
        self.swaps = []
        self.heap = self.build_heap(array)        

    def build_heap(self, array):
        firsParentIdx = (len(array) - 2) // 2

        for currIdx in reversed(range(firsParentIdx + 1)):
            self.siftD(currIdx, len(array)-1, array, task="build")

        return array

    def siftD(self, currIdx, endIdx, heap, task=" "):
        # find children lodes
        child_1 = currIdx*2 + 1

        # continue until child node
        while child_1 <= endIdx:
            child_2 = child_1 + 1 if child_1 + 1 <= endIdx else -1

            # if a child node exists and value of child 2 is smalle than child 1
            if child_2 != -1 and heap[child_2] < heap[child_1]:
                swapIdx = child_2
            else:
                swapIdx = child_1

            # check swapping criteria
            if heap[swapIdx] < heap[currIdx]:
                # swap the positions
                self.swap(currIdx, swapIdx, heap)

                # track the swaps made
                if task.lower() == "build":
                    self.swaps.append([currIdx, swapIdx])

                # update current index and child index
                currIdx = swapIdx
                child_1 = currIdx*2 + 1
            else:
                return

    def siftUp(self, currIdx, heap):
        # find parent index
        parentIdx = (currIdx - 1) // 2

        # continue till at top of heap and value current > value parent  
        while currIdx > 0 and heap[currIdx] < heap[parentIdx]:
            self.swap(currIdx, parentIdx, heap)
            currIdx = parentIdx
            parentIdx = (currIdx - 1) // 2

    def peek(self):
        # return what is at the root
        return self.heap[0]

    def remove(self):
        # swap root and last value, pop, and sift down root to end
        self.swap(0, len(self.heap)-1, self.heap)
        remValue = self.heap.pop()
        self.siftD(0, len(self.heap)-1, self.heap)

        return remValue

    def insert(self, value):
        # attach to end and sift up
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i] 


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps= MinHeap(data)

    print(len(swaps.swaps))
    for i, j in swaps.swaps:
        print(i, j)


if __name__ == "__main__":
    main()
