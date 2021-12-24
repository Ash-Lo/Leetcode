def binary_search(arr, target):
    l, r = 0, len(arr)-1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


## Main
arr = [5, 12, 14, 18, 22, 35, 47, 61]
print('Index = ' + str(binary_search(arr, 35)))
