row = [2, 1, -1, -2, -2, -1, 1, 2, 2]
col = [1, 2, 2, 1, -1, -2, -2, -1, 1]

def isValid(x, y):
    return not (x < 0 or y < 0 or x >= N or y >= N)
def knightTour(visited, x, y, pos, found, count):
    visited[x][y] = pos
    if pos >= N * N:
        for r in visited:
            print(r)
        print()
        found[0] = True    # Tìm thấy giải pháp
        count[0] += 1      # Cộng vào biến count lưu giá trị số giải pháp tìm thấy
        visited[x][y] = 0  # Không tìm thấy giải pháp, quay lui
        return
    for k in range(8):
        newX = x + row[k]
        newY = y + col[k]
        if isValid(newX, newY) and visited[newX][newY] == 0:
            knightTour(visited, newX, newY, pos + 1, found, count)
    visited[x][y] = 0

N = int(input('Nhập N = '))
visited = [[0 for x in range(N)] for y in range(N)]
pos = 1
print('\n__ __ __Nhập vvào vị trí khởi đầu của con mã__ __ __')
print('\t**Lưu ý: Các chỉ số hàng và cột chạy từ 0 đến n-1**')
x, y = int(input('\tNhập vào vị trí hàng ban đầu của con mã: x = ')), int(
        input('\tNhập vào vị trí cột ban đầu của con mã: y = '))

found = [False]
count = [0]
knightTour(visited, x, y, pos, found, count)

if not found[0]:
    print("Không tìm thấy giải pháp")
else:
    print("Số giải pháp: ", count[0])