

class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def __str__(self):
        if self.head is None:
            print('List is empty')
            return
        else:
            list_str = ''
            itr = self.head
            while itr:
                list_str += str(itr.data) + '==>'
                itr = itr.next
            return list_str

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data)

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        if self.head is None:
            return count
        else:
            itr = self.head
            while itr:
                count += 1
                itr = itr.next
            return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')
        elif index == 0:
            self.head = self.head.next
        elif self.head is None:
            print('list is empty')
        else:
            itr = self.head
            for i in range(1, index):
                itr = itr.next
            temp = itr.next
            itr.next = temp.next

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid Index')
        elif index == 0:
            self.insert_at_beginning(data)
        else:
            itr = self.head
            for i in range(1, index):
                itr = itr.next
            temp = itr.next
            itr.next = Node(data, temp)


if __name__ == '__main__':

    llist = LinkedList()
    llist.insert_at_beginning(32)
    llist.insert_values([43, 56, 21])
    llist.insert_at(1, 23)
    print(llist)
    print(llist.get_length())



