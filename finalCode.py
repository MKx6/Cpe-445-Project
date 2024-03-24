class Process:
    # This is class Process to initiate process id, arrival time, burst time
    def __init__(self, pid, at, bt):
        self.pid = pid
        self.arrival = at
        self.burst = bt


def processes(file_name):
    # this function to read the data from existing file includes information of each process
    # information: process id, process arrival time, process burst time
    p = []
    with open(file_name, 'r') as file:
        for line in file:
            pid, arrival_time, burst_time = map(int, line.strip().split())
            p.append((pid, arrival_time, burst_time))
    return p

def fcfs(process):
    # this function represent first come, first served algorithm. then, it calculate average Turnaround Time, average Waiting Time, average Response Time
    current = 0
    wt = {}
    rt = {}
    tt = {}
    chart = []  # List to store execution order

    for pid, arrival_time, burst_time in process:
        if current < arrival_time:
            current = arrival_time
        wt[pid] = current - arrival_time
        if pid not in rt:
            rt[pid] = current - arrival_time
        current += burst_time
        tt[pid] = current - arrival_time
        chart.extend([pid] * burst_time)

    num_process = len(process)
    if num_process != 0:
        avg_wt = sum(wt.values()) / num_process
        avg_rt = sum(rt.values()) / num_process
        avg_tt = sum(tt.values()) / num_process
        print("FCFS result:")
        print("Execution order:", chart)
        print(f"Average Waiting Time: {avg_wt:.2f}")
        print(f"Average Response Time: {avg_rt:.2f}")
        print(f"Average Turnaround Time: {avg_tt:.2f}")
        return current
    else:
        return current


def shift(plist):
    # This function shifts the processes in the queue to assist in handling the round robin algorithm
    temp = plist[0]
    for i in range(len(plist) - 1):
        plist[i] = plist[i + 1]
    plist[len(plist) - 1] = temp
    return plist

def RR(q, process_list, num):
    # round robin function with quantum time
    global chart
    queue = []
    time = 0
    arrived_p = 0  # arrived process
    r_p = 0
    donep = 0  # done process
    start = 0
    wt = {}
    tt = {}
    rt = {}

    while donep < num:
        for i in range(arrived_p, num):
            if time >= process_list[i].arrival:
                queue.append(process_list[i])
                arrived_p += 1
                r_p += 1
        if r_p < 1:
            chart.append(0)
            time += 1
            continue

        if start:
            queue = shift(queue)

        if queue[0].burst > 0:
            if queue[0].burst > q:
                for g in range(time, time + q):
                    chart.append(queue[0].pid)
                time += q
                queue[0].burst -= q
            else:
                for g in range(time, time + queue[0].burst):
                    chart.append(queue[0].pid)
                time += queue[0].burst
                waiting_time = time - queue[0].arrival - queue[0].burst
                wt[queue[0].pid] = waiting_time
                tt[queue[0].pid] = time - queue[0].arrival
                queue[0].burst = 0
                donep += 1
                r_p -= 1
                if queue[0].pid not in rt:
                    rt[queue[0].pid] = time - queue[0].arrival
            start = 1


    avg_wt = sum(wt.values()) / len(wt) if wt else 0
    avg_rt = sum(rt.values()) / len(rt) if rt else 0
    avg_tt = sum(tt.values()) / len(tt) if tt else 0
    return chart, avg_wt, avg_rt, avg_tt

def round_robin(process, quantum=3):
    # round robin function with quantum time = 3, then it prints the result of the function including average turnaround time, average response time, average waiting time
    global chart
    chart = []  # to create gantt chart
    plist = [Process(p[0], p[1], p[2]) for p in process]  # Corrected list comprehension
    n = len(plist)
    result, avg_wt, avg_rt, avg_tt = RR(quantum, plist, n)
    print("Execution order:", result)
    print(f"Average Waiting Time: {avg_wt:.2f}")
    print(f"Average Response Time: {avg_rt:.2f}")
    print(f"Average Turnaround Time: {avg_tt:.2f}")


def srtf(processes):
    # this function represent shortest remaining time first. it results average turnaround time, average response time, average waiting time
    current = 0
    chart = []
    wt = {}
    tt = {}
    rt = {}

    while processes:
        shortest_remaining_time = float('inf')    # sets a variable to positive infinity
        shortest_process = None

        for i, process in enumerate(processes):
            # creates an iterator that generates index-value pairs for each element in the iterable processes
            if process[1] <= current and process[2] < shortest_remaining_time:
                shortest_remaining_time = process[2]
                shortest_process = i

        if shortest_process is not None:
            pid, arrival_time, burst_time = processes[shortest_process]
            if pid not in rt:
                rt[pid] = current - arrival_time
            chart.append(pid)
            current += 1
            burst_time -= 1

            if burst_time == 0:
                tt[pid] = current - arrival_time
                processes.pop(shortest_process)
            else:
                processes[shortest_process] = (pid, arrival_time, burst_time)
                for proc in processes:
                    if proc[1] <= current and proc[0] != pid:
                        wt[proc[0]] = current - proc[1]

        else:
            chart.append(0)
            current += 1


    avg_wt = sum(wt.values()) / len(wt) if wt else 0
    avg_tt = sum(tt.values()) / len(tt) if tt else 0
    avg_rt = sum(rt.values()) / len(rt) if rt else 0

    # Print the results
    print("\nSRTF result:")
    print("Execution order:", chart)
    print(f"Average Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tt:.2f}")
    print(f"Average Response Time: {avg_rt:.2f}")

    return current



if __name__ == "__main__":
    p_file = processes("processes.txt")

    print("\nFCFS")
    fcfs(p_file)

    print("#################################")
    print("\nRR")
    round_robin(p_file)

    print("#################################")
    print("\nSRTF")
    srtf(p_file)

    print("#################################")
