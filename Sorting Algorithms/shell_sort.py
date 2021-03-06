
from random import randint


def shell_sort(arr):

    n = len(arr)
    gap = n//2

    while gap > 0:
        for i in range(gap, n):
            tmp = arr[i]

            j = i
            while j >= gap and arr[j-gap] > tmp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = tmp

        gap //= 2

    return arr


# Tests
if __name__ == '__main__':
    print(shell_sort([randint(0, 1000) for _ in range(10)]))
    print(shell_sort([randint(-500, 500) for _ in range(10)]))

