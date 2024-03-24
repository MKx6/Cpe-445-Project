# Cpe-445-Project

# Team members: 
#Maryam Matar and Ghezlan Alotaibi

This projct is developed by Ghezlan and Maryam, it is a CPU scheduling program that incorporates multiple strategies, including Shortest Remaining Time First (SRTF), First-Come, First-Served (FCFS), Round Robin, and a custom algorithm of our own creation. To run this program, we need an input file containing information about each process, such as the process ID, arrival time, and burst time.

Here's an explanation of each process strategy:

1. First-Come First-Served (FCFS):
FCFS is a non-preemptive scheduling algorithm where processes are executed based on their arrival order. The process that arrives first is executed first, and subsequent processes are executed in the order of their arrival.

2. Round Robin:
Round Robin is a preemptive scheduling algorithm where each process is assigned a fixed time quantum to execute. Once a process's time quantum expires, it is preempted and added back to the end of the ready queue.

3. Shortest Remaining Time First (SRTF):
This strategy selects the process with the shortest remaining burst time to execute next. It is a preemptive scheduling algorithm.

4. Custom algorithm: is a preemptive scheduling algorithm we customize, where processes are prioritizing even process id first,odd id will executed after. 
