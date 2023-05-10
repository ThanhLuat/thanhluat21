def insertion_sort(array, ascending):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        if ascending is True:
            while j >= 0 and key < array[j]:
                array[j+1] = array[j]
                j = j-1
            array[j+1] = key
        else:
            while j >= 0 and key > array[j]:
                array[j+1] = array[j]
                j = j-1
            array[j+1] = key
        print("Sap xep lan thu ", i, ":", array)

if __name__ == "__main__":
    n = abs(int(input("Nhap so phan tu cua array")))
    arr = []
    for i in range(n):
        x = int(input("Nhap phan tu thu" + str(i + 1) +":"))
        arr.append(x)
    is_asc = input("Sap xep theo thu tu tang dan ( True->Tang dan,False->Giam dan ):")
    if is_asc == "True":
        insertion_sort(arr, True)
    elif is_asc == "False":
        insertion_sort(arr, False)