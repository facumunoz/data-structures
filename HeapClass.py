def get_parent_index(child_index):
    return (child_index - 1)//2


def get_left_child_index(parent_index):
    return (parent_index * 2) + 1


def get_right_child_index(parent_index):
    return (parent_index * 2) + 2


class MinHeap(object):
    def __init__(self, capacity= 10):
        self.capacity = capacity
        self.size = 0
        heap_array = [-1]*capacity
        self.heap_array = heap_array

    def has_right_child(self, index):
        return get_right_child_index(index) < self.size

    def has_left_child(self, index):
        return get_left_child_index(index) < self.size

    def has_parent(self, index):
        return get_parent_index(index) >= 0

    def left_child(self, index):
        return self.heap_array[get_left_child_index(index)]

    def right_child(self, index):
        return self.heap_array[get_right_child_index(index)]

    def parent(self, index):
        return self.heap_array[get_parent_index(index)]

    def swap(self, index1, index2):
        temp = self.heap_array[index1]
        self.heap_array[index1] = self.heap_array[index2]
        self.heap_array[index2] = temp

    def peak(self):
        if self.size == 0:
            raise IndexError
        else:
            return self.heap_array[0]

    def pull(self):
        item = self.heap_array[0]
        self.heap_array[0] = self.heap_array[self.size - 1]
        self.size -= 1
        heapify_down()
        return item

    


