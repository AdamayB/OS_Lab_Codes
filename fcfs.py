def fcfs(process,n):
    wt=[0]*n

    index = 0
    for i in range(n - 1):
        index = i
        for j in range(i + 1, n):
            if process[j][0] < process[index][0]:
                index = j

        process[i], process[index] = process[index], process[i]

    bTime = [process[i][1] for i in range(n)]
    wt[0]=0
    ct=[0]*n
    ct[0]=bTime[0]
    for i in range(1,n):
        wt[i]=wt[i-1]+bTime[i-1]
        ct[i]=ct[i-1]+bTime[i]

    return ct,wt

process=[[4, 5],
         [3, 6],
         [1, 7],
         [5, 5]]
print(fcfs(process,4))
