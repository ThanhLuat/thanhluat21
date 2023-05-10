
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            print(f'Buoc {i + 1}: {arr}')
    return arr

data = []
while True:
    num = input("Nhap so (nhap 'x' đe dung nhap):")
    if num == 'x':
        break
    data.append(int(num))
    print("Du lieu hien tai: ", data)
print("Du lieu cuoi cung: ", data)
sorted_arr = selection_sort(data)
print("Ket qua: ", sorted_arr)