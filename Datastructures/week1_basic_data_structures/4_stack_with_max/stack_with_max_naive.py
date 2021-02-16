#python3
import sys

class MinMaxStack():
    def __init__(self):
        # tracker for stack, and new max and min
        self.min_max = []
        self.stack = []

    def push(self, num):
        # use the push function in a list
        track = {"max":num, "min":num}

        if len(self.min_max):
            # extract the most recent minimum and maximum
            prev_min_max = self.min_max[-1]

            # update current
            track["max"] = max(prev_min_max["max"], num)
            track["min"] = min(prev_min_max["min"], num)

        # append boh into array
        self.min_max.append(track)
        self.stack.append(stack)


    def pop(self):
        # use the pop function in a list. pop min_max and stack
        self.min_max.pop()
        return self.stack.pop()

    def peek(self):
        # show whats; ontop currently
        return self.stack[-1]
    
    def getMax(self):
        return self.min_max[-1]["max"]

    def getMin(self):
        return self.min_max[-1]["min"]

if __name__ == '__main__':
    stack = MinMaxStack()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            print(stack.getMax())
        else:
            assert(0)
