#Knuth-Morris-Pratt Algorithm for Substring Search
def prefix_table(string):
    prefix_list=[0]*len(string)
    prefix_list[0]=0
    j=0
    i=1
    indx=1
    while indx<len(prefix_list) and i<len(string):
        if string[j]==string[i]:
            prefix_list[indx]=j+1
            indx+=1
            j+=1
            i+=1
            print("j",j)
            print("i",i)
            if i==len(string)-1 and indx==len(prefix_list)-1:
                #print(i,indx)
                if string[j]==string[i]:
                    prefix_list[indx]=j+1
                    return prefix_list
                else:
                    while j>0:
                        j-=1
                        j=prefix_list[j-1]
                        print("final",j)
                    if string[j]==string[i]:
                        prefix_list[indx]=j+1
                        return prefix_list
                    else:
                        prefix_list[indx]=0
                        return prefix_list

        elif string[j]!=string[i]:
            j=prefix_list[j-1]
            prefix_list[indx]=0
            indx+=1
            i+=1
    return prefix_list

def kmp(s,p):
    n=len(s)
    m=len(p)
    i=0 #for s
    j=0 #for p
    
    prefix=prefix_table(p)
    
    while i<n:
        if s[i]==p[j]:
            if j==m-1:
                return (i-m+1, i)
            i+=1
            j+=1
        
        elif j>0:
            j=prefix[j-1]
        
        else:
            i+=1
            
    return -1
            
kmp('abaaabbbaaaab','abbb')
#Returns (3,5)