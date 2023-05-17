def sequential_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    # Nếu không tìm thấy, trả về -1
    return -1