triangle = [[7], [2, 3], [3,3,1], [3,1,5,4], [3,1,3,1,3], [2,2,2,2,2,2], [5,6,4,5,6,4,3]]


def summer(arr, x=0, y=0, sum=0):
    if x > len(arr) - 1:
        return sum
    if y > len(arr[x]) - 1:
        y = len(arr[x]) - 1

    sum += arr[x][y]

    return max(summer(arr, x+1, y, sum), summer(arr, x+1, y+1, sum))


def summer2(arr):

    for i in range(1, len(arr)):
        arr[-i-1] = [max(y+j, y+z) for y, j, z in zip(arr[-i-1], arr[-i][:-1], arr[-i][1:])]

    return arr[0][0]


print summer(triangle)
print summer2(triangle)