#Given an array of length N find the minimum element in the array

def minElem(arr):
    curr_num=0
    min_num=arr[0]
    for i in range(1,len(arr)):
        curr_num=arr[i]
        if curr_num < min_num:
            min_num=curr_num
    return min_num
