# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers


    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result
class JobScheduler:
    def __init__(self, n_workers, jobs):
        # initialize required workers
        self.workers = self.worker_init(n_workers, len(jobs))

        # jobs
        self.jobs = jobs
        
        # [worker number, start time]
        self.w_heap = self.build_heap(self.workers)
        
        # tracker for jobs, and workers used
        self.track = []

    def worker_init(self, n_workers, n_jobs):
        w_init = []

        # build required number of workers
        for i in range(min(n_workers, n_jobs)):
            # [worker, start time]
            w_init.append([i, 0])

        # returns list
        return w_init

    # assigning jobs
    def assign_jobs(self):
        
        # loop until all jobs assigned
        for i in range(len(self.jobs)):
            # remove top element from heap
            top = self.remove()
            
            # append to the tracking list [worker number, start time, job number]
            #self.track.append([*top, i])

            # append to the tracking list [worker number, start time]
            self.track.append([*top])

            #update the time
            top[1] += self.jobs[i]
            
            # insert in heap
            self.insert(top)
            

        return self.track

    def build_heap(self, w_array):
        firsParentIdx = (len(w_array) - 2) // 2

        for currIdx in reversed(range(firsParentIdx + 1)):
            self.siftD(currIdx, len(w_array)-1, w_array)

        return w_array

    def siftD(self, currIdx, endIdx, w_heap):
        # find children lodes
        child_1 = currIdx*2 + 1

        # continue until child node
        while child_1 <= endIdx:
            child_2 = child_1 + 1 if child_1 + 1 <= endIdx else -1

            check1 = child_2 != -1 and w_heap[child_2][1] < w_heap[child_1][1]
            check2 = child_2 != -1 and w_heap[child_2][1] == w_heap[child_1][1] and w_heap[child_2][0] < w_heap[child_1][0]
            
            # value of array index is = [worker number, start time]
            if check1 or check2 :
                swapIdx = child_2
            else:
                swapIdx = child_1

            # crieria when the current and nex
            # check swapping criteria
            check1 = w_heap[swapIdx][1] < w_heap[currIdx][1]
            check2 = w_heap[swapIdx][1] == w_heap[currIdx][1] and w_heap[swapIdx][0] < w_heap[currIdx][0]

            if check1 or check2:
                # swap the positions
                self.swap(currIdx, swapIdx, w_heap)

                # update current index and child index
                currIdx = swapIdx
                child_1 = currIdx*2 + 1
            else:
                return

    def siftUp(self, currIdx, w_heap):
        # find parent index
        parentIdx = (currIdx - 1) // 2

        check1 = currIdx > 0 and w_heap[currIdx][1] < w_heap[parentIdx][1]
        check2 = currIdx > 0 and w_heap[currIdx][1] == w_heap[parentIdx][1] and w_heap[currIdx][0] < w_heap[parentIdx][0]
        
        # continue till at top of heap and value current < value parent  
        while check1 or check2:
            self.swap(currIdx, parentIdx, w_heap)
            currIdx = parentIdx
            parentIdx = (currIdx - 1) // 2
            
            # perform checks again
            check1 = currIdx > 0 and w_heap[currIdx][1] < w_heap[parentIdx][1]
            check2 = currIdx > 0 and w_heap[currIdx][1] == w_heap[parentIdx][1] and w_heap[currIdx][0] < w_heap[parentIdx][0]

    def peek(self):
        # return what is at the root - 
        return self.w_heap[0]

    def remove(self):
        # swap root and last value, pop, and sift down root to end
        self.swap(0, len(self.w_heap) - 1, self.w_heap)
        remValue = self.w_heap.pop()
        self.siftD(0, len(self.w_heap)-1, self.w_heap)

        # returns [worker number, start time]
        return remValue

    # inser worker into heap
    def insert(self, value):
        # attach to end and sift up
        self.w_heap.append(value)
        self.siftUp(len(self.w_heap) - 1, self.w_heap)

    # swap worker locations
    def swap(self, i, j, w_heap):
        w_heap[i], w_heap[j] = w_heap[j], w_heap[i] 




def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    #assigned_jobs = assign_jobs(n_workers, jobs)

    #for job in assigned_jobs:
    #    print(job.worker, job.started_at)
    jobs = JobScheduler(n_workers, jobs)
    assigned_jobs = jobs.assign_jobs()

    for job in assigned_jobs:
        print(job[0], job[1])

if __name__ == "__main__":
    main()
