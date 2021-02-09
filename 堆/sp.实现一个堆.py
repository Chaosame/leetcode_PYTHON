"""
实现一个最小堆
堆顶总是一个最小值
是一个完全二叉树 一般用一个数组去储存
序号为n的节点它的 孩子节点（如果有） 2n+1 2n+2 父节点(n-1)/2
"""


class Heap:
    data_ = []

    def Minheap(self, heap_list):  # create a min heap from a list
        self.data_ = heap_list
        for i in range((len(heap_list) - 1) // 2, -1,-1):
            self.heapifyDown(i)

    def peak(self):  # return the min element
        return self.data_[0]

    def pop(self):  # extract the min element
        self.data_[0], self.data_[-1] = self.data_[-1], self.data_[0]
        heap_min = self.data_.pop()
        self.heapifyDown(0)
        return heap_min

    def push(self, key):  # add a new element to the heap
        self.data_.append(key)
        self.heapifyUp(len(self.data_) - 1)

    def size(self):  # return size of heap
        return self.data_

    def heapifyUp(self, index):
        if index == 0:  # 到顶了就不用调了递归出口
            return
        parent = (index - 1) / 2  # find parent index
        if self.data_[index] >= self.data_[parent]:
            return
        self.data_[index], self.data_[parent] = self.data_[parent], self.data_[index]
        self.heapifyUp(parent)

    def heapifyDown(self, index):
        min_num = index  # 用于记录最小元素
        # 从左右子树中找一个小的换上来
        for i in [2 * index + 1, 2 * index + 2]:
            if (i < len(self.data_)) and self.data_[i] < self.data_[index]:
                min_num = i
        if min_num == index:  # 没有更新说明不需要动了
            return
        self.data_[min_num], self.data_[index] = self.data_[index], self.data_[min_num]
        self.heapifyDown(min_num)


if __name__ == "__main__":
    heap = Heap()
    TEST = [1, 7, 2, 10, 0, 7, 8]
    heap.Minheap(TEST)
    print(heap.data_)
    print(heap.peak())
