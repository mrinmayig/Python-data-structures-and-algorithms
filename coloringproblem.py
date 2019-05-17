def minPrice(cost):
    lengthofcost=len(cost)
    
    adj=[0]*lengthofcost  
    
    adj[0]=cost[0].index(min(cost[0]))
    
    result=min(cost[0])
    
    i=1
    
    while i<lengthofcost:
        print(i)
        if cost[i].index(min(cost[i]))==adj[i-1]:
            print('if',i)
            if cost[i].index(min(cost[i]))==0:
                result+=min(cost[i][1],cost[i][2])
                adj[i]=cost[i].index(min(cost[i][1],cost[i][2]))
                
                
            elif cost[i].index(min(cost[i]))==1:
                result+=min(cost[i][0],cost[i][2])
                adj[i]=cost[i].index(min(cost[i][0],cost[i][2]))
                
            else:
                result+=min(cost[i][0],cost[i][1])
                adj[i]=cost[i].index(min(cost[i][0],cost[i][1]))
            i+=1                    
        else:
            print('else',i)
            result+=min(cost[i])
            adj[i]=cost[i].index(min(cost[i]))
            i+=1
                            
    return result 

minPrice([[1,2,3],[1,2,3],[1,3,1],[2,3,4],[1,1,1],[6,5,3]])