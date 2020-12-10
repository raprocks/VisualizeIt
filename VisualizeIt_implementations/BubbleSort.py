class BubbleSort:
    def bubblesort(arr, n):
        arr = []*100
        n = int(input("Enter number of elements : "))
        temp = 0
        print("Enter the elements")
        for k in range(0, self.n):
            ele = list(input())
            arr.append(ele)  # adding the element

        for i in range(0, n):
            for j in range(1, n-1):
                if arr[j-1] > arr[j]:
                    # swap elements
                    temp = self.arr[j-1]
                    arr[j-1] = self.arr[j]
                    arr[j] = self.temp

        print("The sorted array is = ")
        for i in range(0, len(arr)):
            print(arr[i])
