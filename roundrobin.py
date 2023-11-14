def round_robin(burst_time, quantum, arrival_time, execution_sequence):
    n = len(burst_time)
    waiting_time = [0] * n
    burst_remaining = burst_time.copy()
    process_index = [0] * n  # Keeps track of where each process left off

    total_time = 0
    execution_sequence.append(0)
    completion_time=[0]*n
    while True:
        done = True
        for i in range(n):
            if arrival_time[i] <= total_time and burst_remaining[i] > 0:
                done = False
                if burst_remaining[i] > quantum:
                    total_time += quantum
                    execution_sequence.append(i)
                    burst_remaining[i] -= quantum
                else:
                    total_time += burst_remaining[i]
                    execution_sequence.append(i)

                    waiting_time[i] = max(0, total_time - arrival_time[i] - burst_time[i])
                    burst_remaining[i] = 0
                    completion_time[i]=total_time

        if done:
            break

    return waiting_time,execution_sequence,completion_time


proc = [1, 2, 3]
n = 3

# Burst time of all processes
burst_time = [10, 5, 8]
arrival_time=[0,0,0]
# Time quantum
quantum = 2;
execution_sequence=[]
print(round_robin(burst_time,quantum,arrival_time,execution_sequence))