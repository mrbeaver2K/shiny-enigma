def quicksort(array, bottom, top):
        if bottom >= top or bottom < 0: 
                return
        p = partition(array, bottom, top) 
        quicksort(array, bottom, p - 1)
        quicksort(array, p + 1, top)

def partition(array, bottom, top):
        pivot = array[top]
        i = bottom - 1
        for j in range(bottom, top):
                if array[j] <= pivot: 
                        i += 1
                        array[i], array[j] = array[j], array[i]
        i += 1
        array[i], array[top] = array[top], array[i]
        return i