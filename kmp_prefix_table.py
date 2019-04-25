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
prefix_table('dsgwadsgz')
#Must return [0,0,0,0,0,1,2,3,0]

prefix_table('abcdabca')
#Must return [0,0,0,0,1,2,3,1]