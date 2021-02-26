

class BubbleSort:
    def __init__(self, arr: list) -> None:
        self.arr = arr
        self.data = {
            'algorithm': {
                'name': "Improved Bubble Sort",
                'type': "Sort"
            },
            'arr': self.arr,
            'array': self.arr.copy(),
            'msg': "Starting The Algorithm",
            'comparing': False,
            'swapping': False,
            'sorted': False,
            'pass': 1,
            'comparisons': 0,
            'swaps': 0,
            'comparing_data': {'comp_a': 0, 'comp_b': 1},
            'swapping_data': {'a_idx': 0, 'b_idx': 1}
        }

    def sort(self):
        self.data['current_array'] = self.arr
        self.data['fixed'] = len(self.arr)-1
        yield self.data
        for i in range(0, len(self.arr)):
            self.data['pass'] = i+1
            yield self.data
            sorted = True
            for j in range(1, len(self.arr)-i):
                self.data['comparing'] = True
                self.data['comparing_data'] = {'comp_a': j-1, 'comp_b': j}
                self.data['comparisons'] += 1
                yield self.data
                if self.arr[j-1] > self.arr[j]:
                    sorted = False
                    self.data['msg'] = str(self.arr[j-1]) + " is greater than " \
                        + str(self.arr[j]) + ", gonna swap"
                    self.data['swaps'] += 1
                    self.data['comparing'] = False
                    self.data['swapping'] = True
                    self.data['swapping_data'] = {'a_idx': j-1, 'b_idx': j}
                    yield self.data
                    self.data['swapping'] = False
                    self.arr[j-1], self.arr[j] = self.arr[j], self.arr[j-1]
                    self.data['msg'] = f"swapped element at {j} and {j-1}"
                    yield self.data
            self.data['fixed'] -= 1
            if sorted:
                self.data['sorted'] = True
                self.data['msg'] = "Successfully Sorted the Array"
                self.data['fixed'] = -1
                yield self.data
        self.data['sorted'] = True
        self.data['msg'] = "Successfully Sorted the Array"
        yield self.data
