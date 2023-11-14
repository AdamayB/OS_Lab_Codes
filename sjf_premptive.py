def findWaitingTime(processes,n,wt):
    rt=[0]*n
    ct=[0]*n
    for i in range(n):
        rt[i]=processes[i][1]

    complete=0
    t=0
    minm=999999999
    short=0
    check=False

    while complete!=n:
        for j in range(n):
            if (processes[j][2]<=t) and (rt[j]<minm and rt[j]>0):
                minm=rt[j]
                short = j
                check = True
        if check==False:
            t+=1
            continue

        rt[short]-=1
        minm=rt[short]
        if(minm==0):
            minm=999999999

        if (rt[short]==0):
            complete+=1
            check = False

            fint=t+1

            wt[short]= fint-proc[short][1]-proc[short][2]
            ct[short]=fint

            if wt[short]<0:
                wt[short]=0

        t+=1

    return wt,ct
#       PNo BT AT
proc = [[1, 6, 1],
        [2, 8, 1],
        [3, 7, 2],
        [4, 3, 3]]
n = 4
wt=[0]*n
waiting_time,ct=findWaitingTime(proc, n,wt)
print(waiting_time,ct)

