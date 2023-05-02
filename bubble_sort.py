def bubble_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len):
        for j in range(0, arr_len-1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    return arr

print("BUBBLE SORT ALGORITHM")
is_stop = True
num_arr = []
while is_stop:
    num_input = input("Write list of number. Input X to stop: ")
    if num_input == 'X' or num_input == 'x':
        is_stop == False
        break
    num_arr.append(int(num_input))

sorted_arr = bubble_sort(num_arr)
print("Sorted array: {}".format(sorted_arr))
    