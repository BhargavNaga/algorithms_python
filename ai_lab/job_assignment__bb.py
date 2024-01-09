from heapq import heappush, heappop
n = 4
import copy
global allocated
allocated = [False]*n

class priorityQueue:
	
	
	def __init__(self):
		self.heap = []


	def push(self, k):
		heappush(self.heap, k)

	def pop(self):
		return heappop(self.heap)
     
     # make heap empty


	def empty(self):
		if not self.heap:
			return True
		else:
			return False

class node:
    def __init__(self,workernum,jobnum,parent):
        self.workernum = workernum
        self.jobnum = jobnum
        self.parent = parent
        self.cost_estimated = 0
        self.cost = 0
        self.assigned = [False]*n
        global allocated
        self.allocated = allocated

    def __lt__(self, nxt):
        return self.cost_estimated < nxt.cost_estimated
    
def newnode(i,j,parent):
    node2 = node(i,j,parent)
    if j != -1:
     node2.assigned[j] = True
    return node2

def printAssignment(min_node):
    if min_node.parent is None:
        return
    printAssignment(min_node.parent)
    print(f"Assign Worker {chr(min_node.workernum + 65)} to Job {min_node.jobnum}")

   # assigned[min_node.jobnum] = True
    return

def calculateCost(cost_matrix, x, y, assigned):
    cost =0
    available = [True]*n

    for i in range(x+1,n):
        min = float('inf')
        min_index = -1
        for j in range(n):
            if not assigned[j] and available[j] and cost_matrix[i][j] < min:
                min_index = j
                min = cost_matrix[i][j]
        cost += min
        available[min_index] = False
    return cost
         


def job_assignment(cost_matrix):

    pq = priorityQueue()
    root = newnode(-1,-1,None)
    pq.push(root)
	

    while not pq.empty():
        min_node = pq.pop()

        i = min_node.workernum+1
        if i != 0:
         min_node.allocated[min_node.jobnum] = True
        if i == n:
            printAssignment(min_node)
            return min_node.cost
        
        for j in range(n):
            if not min_node.allocated[j]:
                child = newnode(i,j,min_node)
                child.cost = min_node.cost + cost_matrix[i][j]
                child.cost_estimated = child.cost + calculateCost(cost_matrix,i,j,child.assigned)
                pq.push(child)

	


if __name__ == '__main__':

    # driver code
    cost_matrix = [[9, 2, 7, 8],[6, 4, 3, 7],[5, 8, 1, 8],[7, 6, 9, 4]]
    print("cost matrix")
    print(cost_matrix)
    print("min cost")
    print(job_assignment(cost_matrix))

