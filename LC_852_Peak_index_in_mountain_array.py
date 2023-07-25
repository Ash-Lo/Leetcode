class PeakArrayIndex:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        l, r = 0, len(arr) - 1
        res = -1
        while l <= r:
            m = l + ((r-l) // 2)
            if arr[m] > arr[m+1]:  # Descending part
                res = m
                r = m - 1
            elif arr[m] < arr[m+1]:  # Ascending part
                l = m + 1
        return res


request = PeakArrayIndex()
arr = [0, 10, 5, 2]
print(request.peakIndexInMountainArray(arr))
