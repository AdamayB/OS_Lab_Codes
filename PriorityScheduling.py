def findWaitingTime(processes, n, wt):
    wt[0] = 0
    ct=[0]*n
    ct[0]=processes[0][1]
    # calculating waiting time
    for i in range(1, n):
        wt[i] = processes[i - 1][1] + wt[i - 1]
        ct[i]=processes[i][1]+wt[i]
    return wt,ct

def priorityScheduling(proc, n):
    # Sort processes by priority
    wt = [0] * n
    proc = sorted(proc, key=lambda proc: proc[2],
                  reverse=True)

    print("Order in which processes gets executed")
    for i in proc:
        print(i[0], end=" ")
    print(findWaitingTime(proc, n,wt))

proc = [[1, 10, 1],
        [2, 5, 3],
        [3, 8, 2]]
n = 3

priorityScheduling(proc, n)