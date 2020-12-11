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
            'process_data': {},
            'searching': True,
            'msg': "Starting the algo"
        }

    def step_search(self, element: int):
        self.data['found'] = False
        start, end = 0, len(self.arr)-1
        self.data['process_data'] = {'start': start, 'end': end}
        mid = (start + end) // 2
        self.data['process_data']['mid'] = mid
        self.data['searching'] = True
        while start <= end:

            if self.arr[mid] < element:
                self.data['comparing'] = True
                self.data['comparing_data'] = {
                    'ele1': self.arr[mid],
                    'ele2': element}
                start = mid+1
                self.data['msg'] = f"setting start to {start}"
                yield self.data

            elif self.arr[mid] > element:
                self.data['comparing'] = True
                self.data['comparing_data'] = {
                    'ele1': self.arr[mid],
                    'ele2': element}
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
            self.data['msg'] = f"{element} not found in {self.arr}"
            return self.data
