def first_non_consecutive(arr):
    for i in range(len(arr)):
        if arr[i] - arr[i-1] > 1:
            print (arr[i]-1, 'is missing')

arr=[483,484,485,486,488,489,490,491,492,493]
first_non_consecutive(arr)