def insertion_sort(arr):
    n = len(arr)
    for i in range (1, n):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            j = j-1
    return arr

print("INSERTION SORT ALGORITHM")
is_stop = True
num_arr = []
while is_stop:
    num_input = input("Write list of number. Input X to stop: ")
    if num_input == 'X' or num_input == 'x':
        is_stop == False
        break
    num_arr.append(int(num_input))

sorted_arr = insertion_sort(num_arr)
print("Sorted array: {}".format(sorted_arr))