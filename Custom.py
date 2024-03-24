class Process:
    def __init__(self, pid, at, bt):
        self.pid = pid
        self.arrival = at
        self.burst = bt


def processes(filename):
    p = []
    with open(filename, 'r') as file:
        for line in file:
            pid, arrival_time, burst_time = map(int, line.strip().split())
            p.append(Process(pid, arrival_time, burst_time))
    return p


def custom_preemptive(proc):
    current = 0
    queue = []
    chart = []
    wt = {}
    tt = {}

    def get_priority(proc):
        if proc.pid % 2 == 0:  # Even process
            return -proc.arrival
        else:  # Odd process
            return float('inf')

    for process in proc:
        process.remaining_burst = process.burst

    while proc or queue:
        for process in proc:
            if process.arrival <= current:
                queue.append(process)
                proc.remove(process)

        if not queue:
            chart.append(0)
            current += 1
            continue

        queue.sort(key=get_priority)  # Sort by priority (even processes first)

        shortest_process = queue[0]
        chart.append(shortest_process.pid)
        if shortest_process.pid not in wt:
            wt[shortest_process.pid] = current - shortest_process.arrival
        current += 1
        shortest_process.remaining_burst -= 1

        if shortest_process.remaining_burst == 0:
            tt[shortest_process.pid] = current - shortest_process.arrival
            queue.remove(shortest_process)


    avg_wt = sum(wt.values()) / len(wt) if wt else 0
    avg_tt = sum(tt.values()) / len(tt) if tt else 0

    # Print results
    print("Execution order:", chart)
    print(f"Average Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tt:.2f}")



if __name__ == "__main__":
    p_file = processes("processes.txt")

    print("\nCustom Preemptive")
    custom_preemptive(p_file)
