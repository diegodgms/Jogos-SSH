lista = [5,3,4,6,8,25,36,32,8,61,5,45,2156,4874,1,84,89,21,84,84,65,4,8,84,31,84,9,4,4,]

def bubble_sort(arr):
    n = len(arr)
    print(n)

    for i in range(n):
       for j in range(0, n-i-1):
           if arr[j] > arr[j+1]:
               arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

print(bubble_sort(lista))