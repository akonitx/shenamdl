def sharp_piramide(
        height: int,
        block: str | int) -> None:
    """Printing piramide with the str or int object and height that you entered. 

    Each level is increminting by one object(item) and returns this result to use for next level incrementing by one obj(item) and so on."""

    y = ""
    for i in range(height):
        y += str(block)
        print(y)


def factorial(num: int) -> int:
    """Returns factorial from num argument."""
    result = 1
    mid_result = [result := result * y for y in range(1, num + 1)]
    return result


def selectionSort(array):
    size = len(array)
    for s in range(size):
        min_idx = s

        for i in range(s + 1, size):

            # For sorting in descending order
            # for minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i

        # Arranging min at the correct position
        array[s], array[min_idx] = array[min_idx], array[s]
    return array


def bubbleSort(arr):

    ln: int = len(arr)

    for i in range(ln):
        y = ln - i - 1  # huy
        for j in range(0, y):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def log2n(n: int) -> int:
    """Return how many iterations of divisions by 2 we need to get value of 1 of entered number

    :param int n: number which will be divided by 2
    :return int: numbers of iterations to get value 1 of division n by 2
    """
    iten = 0
    while n > 1:
        n = int(n/2)
        iten += 1
    return iten


def insertionSort(list1):

    # Outer loop to traverse on len(list1)
    for i in range(1, len(list1)):

        y = list1[i]

        # Move elements of list1[0 to i-1],
        # which are greater to one position
        # ahead of their current position
        j = i - 1

        while j >= 0 and y < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1

        list1[j + 1] = y

    return list1


def bucketSort(y):
    arr = []
    slot_num = 10  # 10 means 10 slots, each
    # slot's size is 0.1
    for i in range(slot_num):
        arr.append([])

    # Put array elements in different buckets
    for j in y:
        index_b = int(slot_num * j)
        arr[index_b].append(j)

    # Sort individual buckets
    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])

    # concatenate the result
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            y[k] = arr[i][j]
            k += 1
    return y

# Python program for the above approach

# Bucket sort for numbers
# having integer part


def bucketIntSort(arr, nummbe_of_buckets):
    max_ele = max(arr)
    min_ele = min(arr)

    # range(for buckets)
    rnge = (max_ele - min_ele) / nummbe_of_buckets

    temp = []

    # create empty buckets
    for i in range(nummbe_of_buckets):
        temp.append([])

    # scatter the array elements
    # into the correct bucket
    for i in range(len(arr)):
        y = (arr[i] - min_ele) / rnge
        diff = y - int(y)

        # append the boundary elements to the lower array
        if (diff == 0 and arr[i] != min_ele):
            temp[int(y) - 1].append(arr[i])

        else:
            temp[int(y)].append(arr[i])

    # Sort each bucket individually
    for i in range(len(temp)):
        if len(temp[i]) != 0:
            temp[i].sort()

    # Gather sorted elements
    # to the original array
    k = 0
    for lst in temp:
        if lst:
            for i in lst:
                k1 = k
                arr[k1] = i
                k1 += 1


y = False

y = True
if y:
    y = 2 + 3 + 6

if __name__ == "__main__":
    ...  # nothing to do else
