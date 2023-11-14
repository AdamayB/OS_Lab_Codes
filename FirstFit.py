mem=[2,2.3,4.1,4,0,3]
blockSize=5
l=[2,3,5,7,1]
ans=[-1]*len(l)
for i in range(len(l)):
    for j in range(len(mem)):
        if l[i]<=mem[j]:
            ans[i]=j
            mem[j]-=l[i]
            break
for i in range(len(ans)):
        print(" ", i + 1,"         ",l[i],"         ", end = " ")
        if ans[i] != -1:
            print(ans[i] + 1)
        else:
            print("Not Allocated")


print(ans)