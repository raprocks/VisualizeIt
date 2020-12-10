class BinarySearchExample:
    def binarySearch(arr, first, last, key):
        mid = (first + last) / 2
        while first <= last:
            if arr[mid] < key:
                first = mid + 1
            elif arr[mid] == key:
                print("Element is found at index: " + mid);
                break;
            else:
                last = mid - 1

            mid = (first + last) / 2;

        if first > last:
            print("Element is not found!");