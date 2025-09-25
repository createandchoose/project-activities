numbers = [-1, 0, 3, 5, 9, 12]
target = int(input("таргет: "))
left = 0
right = len(numbers) - 1
result = -1
while left <= right:
    mid = (left + right) // 2
    if numbers[mid] == target:
        result = mid
        break
    elif numbers[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

print(result)