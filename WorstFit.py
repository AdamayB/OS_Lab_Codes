mem=[2,2.3,4.1,4,0,3]
l=[2,3,5,7,1]
m=len(mem)
n=len(l)
allocation=[-1]*n
for i in range(n):
    idx=-1
    for j in range(m):
        if mem[j]>=l[i]:
            if idx == -1:
                idx = j
            elif mem[idx] < mem[j]:
                idx = j

    if idx != -1:
        allocation[i] = idx
        mem[idx] -= l[i]

print("Process No. Process Size     Block no.")
for i in range(n):
    print(i + 1, "                  ", l[i],end = "         ")
    if allocation[i] != -1:
        print(allocation[i] + 1)
    else:
        print("Not Allocated")