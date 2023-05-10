def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(f"Buoc {i+1}: {arr}")

arr = []
while True:
    num = input("Nhap so (nhap 'x' de dung nhap):")
    if num == 'x':
        break
    arr.append(int(num))
print("Du lieu ban dau: ", arr)
bubble_sort(arr)
print("Du lieu sau khi sap xep:", arr)