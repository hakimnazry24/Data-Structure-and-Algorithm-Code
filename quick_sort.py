def main():
    print("SELECTION SORT ALGORITHM")
    is_continue = True
    num_arr = []
    n = len(num_arr)

    while is_continue:
        num_input = input("Write list of number. Input X to stop: ")
        if num_input == 'X' or num_input == 'x':
            is_continue == False
            break
        num_arr.append(int(num_input))

    sorted_arr = quick_sort(num_arr, 0, n-1)
    print("Sorted array: {}".format(sorted_arr))

def quick_sort(arr, start, end):
    if end <= start:
        return
    pivot = partition(arr, start, end)
    quick_sort(arr, start, pivot-1)
    quick_sort(arr, pivot+1, end)
    
def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1


    return i
main()