
class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.insert(0, item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
    def peek(self):
        if not self.is_empty():
            return self.items[0]
    def size(self):
        return len(self.items)

s = Stack()

while True:
    print('Nhập vào một số nguyên: ')
    input_num = input()
    try:
        num = int(input_num)
    except ValueError:
        print('Bị lỗi! Bạn phải nhập vào một số nguyên.')
        continue
    s.push(num)
    print(f'Đã thêm số {num} vào ngăn xếp.')
    print(f'Ngăn xếp hiện tại: {s.items}')
    print('Bạn có muốn nhập tiếp không? (có/không)')
    choice = input()

    if choice.lower() == 'không':
        break
while not s.is_empty():
    num = s.pop()
    print(f'Đã lấy số {num} ra khỏi ngăn xếp.')
    print(f'Ngăn xếp hiện tại: {s.items}')