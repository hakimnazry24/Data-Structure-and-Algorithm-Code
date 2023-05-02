def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        #swap
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print("SELECTION SORT ALGORITHM")
is_stop = True
num_arr = []
while is_stop:
    num_input = input("Write list of number. Input X to stop: ")
    if num_input == 'X' or num_input == 'x':
        is_stop == False
        break
    num_arr.append(int(num_input))

sorted_arr = selection_sort(num_arr)
print("Sorted array: {}".format(sorted_arr))