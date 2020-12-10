from typing import Union


class BinarySearch:
    def __init__(self, arr: Union[list, tuple]):
        self.arr = arr
        self.data = {
            'algorithm': {
                'type': 'search',
                'name': 'Binary Search',
            },
            'array': self.arr,
            'process_data': {}
        }

    def step_search(self, element: int):
        self.data['found'] = False
        start, end = 0, len(self.arr)-1
        self.data['process_data'] = {'start': start, 'end': end}
        mid = (start + end) // 2
        self.data['process_data']['mid'] = mid
        self.data['searching'] = True
        while start <= end:
            self.data['searching'] = False
            if self.arr[mid] < element:
                self.data['comparing'] = True
                self.data['comparing_data'] = {
                    'ele1': self.arr[mid],
                    'ele2': element}
                self.data['msg'] = f"{self.data['comparing_data']['ele1'] if self.data['comparing_data']['ele1'] < self.data['comparing_data']['ele2'] else self.data['comparing_data']['ele2']} is smaller"
                start = mid+1
                self.data['msg'] = f"setting start to {start}"
                yield self.data

            elif self.arr[mid] > element:
                self.data['comparing'] = True
                self.data['comparing_data'] = {
                    'ele1': self.arr[mid],
                    'ele2': element}
                self.data['msg'] = f"{self.data['comparing_data']['ele1'] if self.data['comparing_data']['ele1'] > self.data['comparing_data']['ele2'] else self.data['comparing_data']['ele2']} is greater"
                end = mid-1
                self.data['msg'] = f"setting end to {end}"
                yield self.data
            elif self.arr[mid] == element:
                self.data['found'] = True
                return self.data
            mid = (start+end)//2
            self.data['msg'] = f"setting mid to {mid}"
            yield self.data
        if start > end:
            self.data['searching'] = False
            self.data['found'] = False
            return self.data

    def binarySearch(self, arr, first, last, key):
        mid = (first + last) / 2
        while first <= last:
            if arr[mid] < key:
                first = mid + 1
            elif arr[mid] == key:
                print("Element is found at index: " + mid)
                break
            else:
                last = mid - 1

            mid = (first + last) / 2

        if first > last:
            print("Element is not found!")
