class MyHashMap:

    def __init__(self):
        self.map = []

    def put(self, key: int, value: int) -> None:
        match_flag = 0
        for pair in self.map:
            if pair[0] == key:
                pair[1] = value
                match_flag = 1
        if not match_flag:
            self.map.append([key,value])

    def get(self, key: int) -> int:
        for pair in self.map:
            if pair[0] == key:
                return pair[1]

        return -1

    def remove(self, key: int) -> None:
        for i , pair in enumerate(self.map):
            if pair[0] == key:
                del self.map[i]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


## Main
# arr = [[1, 4], [2, 1], [3, 5]]
# print(arr)
# for i,val in enumerate(arr):
#     print(i, val[0])
# del arr[1]
# print(arr)