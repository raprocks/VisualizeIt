from typing import Union


class BinarySearch:
    def __init__(self, arr: Union[list, tuple]):
        self.arr = arr
        self.data = {
            'algorithm': {
                'type': 'Search',
                'name': 'Binary Search',
            },
            'array': self.arr.copy(),
            'process_data': {},
            'searching': True,
            'msg': "Starting the Algorithm",
            'notfound': False
        }

    def step_search(self, element: int):
        self.data['found'] = False
        start, end = 0, len(self.arr)-1
        self.data['process_data'] = {'start': start, 'end': end}
        mid = (start + end) // 2
        self.data['process_data']['mid'] = mid
        self.data['searching'] = True
        yield self.data
        self.data['msg'] = f'''Current Start is {
                start}, Mid is {mid} and End is {end}'''
        while start <= end:
            if self.arr[mid] < element:
                self.data['comparing'] = True
                self.data['comparing_data'] = {
                    'ele1': self.arr[mid],
                    'ele2': element
                }
                start = mid+1
                self.data['msg'] = f"Setting 'start' to {start}"
                self.data['process_data']['start'] = start
                yield self.data

            elif self.arr[mid] > element:
                self.data['comparing'] = True
                self.data['comparing_data'] = {
                    'ele1': self.arr[mid],
                    'ele2': element}
                end = mid-1
                self.data['msg'] = f"Setting 'end' to {end}"
                self.data['process_data']['end'] = end
                yield self.data
            elif self.arr[mid] == element:
                self.data['found'] = True
                self.data['searching'] = False
                self.data['msg'] = f"{element} Found at Index {mid}"
                return self.data
            mid = (start+end)//2
            self.data['process_data']['mid'] = mid
            self.data['msg'] = f"Setting 'mid' to {mid}"
            yield self.data
        if start > end:
            self.data['searching'] = False
            self.data['found'] = False
            self.data['notfound'] = True
            self.data['msg'] = f"{element} Not Found in {self.arr}"
            return self.data
