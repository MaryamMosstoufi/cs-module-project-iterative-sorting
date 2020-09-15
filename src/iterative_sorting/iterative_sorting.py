# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # cur_index = i
        # smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    keep_swapping = True
    while keep_swapping:
        keep_swapping = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                keep_swapping = True

    return arr


# def bubble_sort(arr):
#     le = len(arr)
#     # Loop through all indices
#     for i in range(le):
#         # len - i because we are "moving" through the list
#         # i.e. if le = 6 and we are at index 4 only 2 items remain
#         # then -1 because x+1 on last element will be out of range
#         for x in range(le - i - 1):
#             # If left element is greater than right element
#             if arr[x] > arr[x+1]:
#                 # swap
#                 arr[x], arr[x+1] = arr[x+1], arr[x]
#     return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


# def counting_sort(arr, maximum=None):
#     if len(arr) <= 1:
#         return arr
#     else:
#         count = {}
#         for i in range(0, len(arr)):
#             count[arr[i]] += 1
#         sorted = []
#         for i in count:
#             for j in range(0, count[i]):
#                 sorted.push.

#     return arr
