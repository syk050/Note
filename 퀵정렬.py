def quick_sort(array, start, end):
    # 원소가 한개인 경우
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    # 교차하지 않을 동안
    while left <= right:
        # 큰 값을 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 작은 값을 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        # 교차시 피봇과 작은 값을 교환
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 큰 값과 작은 값 교환
        else:
            array[left], array[right] = array[right], array[left]

    # 왼쪽 배열 오른쪽 배열 분할
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


def quick_sort2(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if pivot >= x]
    rigth_side = [x for x in tail if x > pivot]

    return quick_sort2(left_side) + [pivot] + quick_sort2(rigth_side)


data = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

quick_sort(data, 0, len(data)-1)
print(data)

data = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
print(quick_sort2(data))
