def findWaitingTime(processes,n,bt,wt):
    wt[0]=0
    ct=[0]*n
    ct[0]=bt[0]
    for i in range(1,n):
        wt[i]=bt[i-1]+wt[i-1]
        ct[i]=ct[i-1]+bt[i]

    return wt,ct


processes = [1, 2, 3]
n = len(processes)

# Burst time of all processes
burst_time = [10, 5, 8]
wt=[0]*n
print(findWaitingTime(processes, n, burst_time,wt))