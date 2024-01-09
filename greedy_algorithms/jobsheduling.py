import heapq


def jobScheduling_profit(arr):
    arr.sort(key=lambda x: x[2], reverse=True)
    
    max_deadline = max(arr, key=lambda x: x[1])[1]
    print(max_deadline)
    slots = [-1]*(max_deadline)


    for i in range(len(arr)):
        for j in range(arr[i][1]-1,-1,-1):
            # add job to rightmost slot available
            # if deadline is 3, then add job to 2nd index if available else 1st index if available else 0th index
            if slots[j] == -1:
                slots[j] = arr[i][0]
                break
    return slots

def jobScheduling_deadlines(arr):
    arr.sort(key=lambda x: x[1])
    max_deadline = max(arr, key=lambda x: x[1])[1]
    print(max_deadline)
    slots = [-1]*(max_deadline)
    

if __name__ == '__main__':
    
    arr = [['a',2,100],['b',1,19],['c',10,27],['d',1,25],['e',3,15]]

    print("greedy -1 jobsheduling via profits",jobScheduling_profit(arr))
   # print("greedy -2 jobsheduling via deadlines",jobScheduling_deadlines(arr))
    
'''
    import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        heapq.heappush(self.heap, -value)

    def pop(self):
        return -heapq.heappop(self.heap)

# Example usage:
max_heap = MaxHeap()
values_to_insert = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Insert values into the max heap
for value in values_to_insert:
    max_heap.push(value)

print("Max Heap elements:")
while max_heap.heap:
    print(max_heap.pop())

    
    '''