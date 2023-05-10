class Queue:
    def __init__(self, max):
        self.front = 0
        self.rear = max - 1
        self.size = 0
        self.items = [None] * max
        self.max = max
    def is_empty(self):
        return self.size == 0
    def is_full(self):
        return self.size == self.max
    def enqueue(self, item):
        if self.is_full():
            print('Hang doi day')
            return
        self.rear = (self.rear + 1) % self.max
        self.items[self.rear] = item
        self.size += 1
        print('% s duoc them vao hang doi' % str(item))

    def dequeue(self):
        if self.is_empty():
            print("Hang doi rong")
            return None
        item = self.items[self.front]
        self.front = (self.front + 1) % self.max
        self.size -= 1
        return item

    def front_q(self):
        if self.is_empty():
            return None
        return self.items[self.front]
    def size_q(self):
        return self.size

    def print_q(self):
        if self.is_empty():
            return "Hang doi day"
        return ', '.join(str(item) for item in self.items[self.front:self.rear + 1])


queue = Queue(abs(int(input('Max queue la:'))))
print('Queue co rong hay khong:', queue.is_empty())
n = abs(int(input('Nhap so phan tu them vao queue:')))

for i in range(n):
    queue.enqueue(int(input('Nhap vao 1 so nguyen:')))
queue.enqueue(int(input('Them 1 so nguyen khac vao queue:')))
print('Loai bo va tra ve phan tu đau tien:', queue.dequeue())
print('Tra ve phen tu đau tien:', queue.front_q())
print('Queue hien tai:', queue.print_q())
print('Size của queue:', queue.size_q())