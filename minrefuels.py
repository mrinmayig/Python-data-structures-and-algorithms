#Minimum number of stops at gas stations using Greedy Algorithm
#Time Complexity: O(n)

def minRefills(arr,distance):

    """Given a sorted array of length n and distance 
    that can be traveled with a full fuel tank,
    return the minimum number of refuels needed 
    on the way to get to the destination"""
    
    numRefills=0
    n=len(arr)-1
    currRefill=0
    lastRefill=0 
    
    while currRefill <= n:
        
        while currRefill<n and (arr[currRefill+1]-arr[lastRefill]) <= distance:
            currRefill += 1
            
        lastRefill=currRefill 
        currRefill += 1
        
        if currRefill<=n:
            numRefills += 1     
            
        if currRefill<=n and arr[currRefill]-arr[lastRefill]>distance:
            return "It is not possible to get to the end"
            
    return numRefills

minRefills([3,5,7,10,12,15],5)
#Function returns 2