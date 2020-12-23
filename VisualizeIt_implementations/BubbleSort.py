from typing import Union


class BubbleSort:
    def __init__(self, arr: Union[list, tuple]):
        self.arr = arr
        self.data = {
            'algorithm': {
                'name': "Bubble Sort",
                'type': "Sort"
            },
            'arr': self.arr,
            'array': self.arr.copy(),
            'msg': "Starting The Algorithm",
            'comparing': False,
            'swapping': False,
            'sorted': False,
            'pass': 0,
            'comparing_data': {'comp_a': 0, 'comp_b': 1},
            'swapping_data': {'a_idx': 0, 'b_idx': 1}
        }

    def sort(self):
        yield self.data
        self.data['current_array'] = self.arr
        for i in range(0, len(self.arr)):
            self.data['pass'] = i
            yield self.data
            for j in range(1, len(self.arr)-i):
                self.data['comparing'] = True
                self.data['comparing_data'] = {'comp_a': j-1, 'comp_b': j}
                yield self.data
                if self.arr[j-1] > self.arr[j]:
                    self.data['msg'] = f"{self.arr[j-1]} is greater than {self.arr[j]}, gonna swap"
                    self.data['comparing'] = False
                    self.data['swapping'] = True
                    self.data['swapping_data'] = {'a_idx': j-1, 'b_idx': j}
                    yield self.data
                    self.data['swapping'] = False
                    self.arr[j-1], self.arr[j] = self.arr[j], self.arr[j-1]
                    self.data['msg'] = f"swapped element at {j} and {j-1}"
                    yield self.data
        self.data['sorted'] = True
        yield self.data
