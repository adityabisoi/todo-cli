import pickle

filename = 'storage.pk'

class MinHeap:
    def __init__(self,arr):
        self.arr=arr
        self.size=len(arr)

    def getParentIndex(self,index):
        return (index-1)//2
    
    def getLeftChildIndex(self,index):
        return 2*index+1

    def getRightChildIndex(self,index):
        return 2*index+2

    def getParentPriority(self,index):
        return self.arr[self.getParentIndex(index)][0]
    
    def getLeftChildPriority(self,index):
        return self.arr[self.getLeftChildIndex(index)][0]

    def getRightChildPriority(self,index):
        return self.arr[self.getRightChildIndex(index)][0]

    def getPriority(self,index):
        return self.arr[index][0]

    def hasParent(self,index):
        return self.getParentIndex(index)>=0
    
    def hasLeftChild(self,index):
        return self.getLeftChildIndex(index)<self.size

    def hasRightChild(self,index):
        return self.getRightChildIndex(index)<self.size
    
    def swap(self,index1,index2):
        self.arr[index1],self.arr[index2]=self.arr[index2],self.arr[index1]
    
    def getTask(self):
        if not self.arr:
            return 'No more tasks to do, enjoy the rest of your day;)'
        task=self.arr[0][1]
        if len(self.arr)==1:
            self.arr.pop()
        else:
            self.arr[0]=self.arr.pop()
        self.size-=1
        self.heapifyDown()
        return task
    
    def heapifyDown(self):
        i=0
        while self.hasLeftChild(i):
            minIndex=self.getLeftChildIndex(i)
            if self.hasRightChild(i) and self.getRightChildPriority(i)<self.getLeftChildPriority(i):
                minIndex=self.getRightChildIndex(i)
            if self.getPriority(i)<self.getPriority(minIndex):
                break
            else:
                self.swap(i, minIndex)
            i=minIndex
            
    def addTask(self,priority,taskName):
        self.arr.append((priority,taskName))
        self.size+=1
        self.heapifyUp()

    def heapifyUp(self):
        i=self.size-1
        while self.hasParent(i):
            parentIndex=self.getParentIndex(i)
            if self.getParentPriority(i)>self.getPriority(i):
                self.swap(i,parentIndex)
            else:
                break
            i=parentIndex

    def returnHeap(self):
        return self.arr


def addToHeap(task,priority):
    try:
        with open(filename, 'rb') as fi:
            arr=pickle.load(fi)
    except Exception:
            arr=[]
    heap=MinHeap(arr)
    heap.addTask(priority, task)
    arr=heap.returnHeap()
    with open(filename,'wb') as fi:
        pickle.dump(arr, fi)

def removeFromHeap():
    try:
        with open(filename, 'rb') as fi:
            arr=pickle.load(fi)
    except Exception:
            return 'No more tasks to do, enjoy the rest of your day;)'
    heap=MinHeap(arr)
    task = heap.getTask()
    arr=heap.returnHeap()
    with open(filename,'wb') as fi:
        pickle.dump(arr, fi)
    return task