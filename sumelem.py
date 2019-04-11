#Given an array of size N return the sum of all its elements

def sumofele(arr):
    curr_sum=arr[0]
    for i in range(1,len(arr)):
        curr_sum = curr_sum + arr[i]
    return curr_sum
    