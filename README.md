# Cpe-445-Project

# Team members: 
Maryam Matar 2201127518
Ghezlan Alotaibi 2192131066

This project is CPU scheduling program that incorporates multiple strategies, including Shortest Remaining Time First (SRTF), First-Come, First-Served (FCFS), Round Robin, and a custom algorithm of our own creation. To run this program, we need an input file containing information about each process, such as the process ID, arrival time, and burst time.
Here's an explanation of each process strategy:

1. First-Come First-Served (FCFS):
FCFS is a non-preemptive scheduling algorithm where processes are executed based on their arrival order. The process that arrives first is executed first, and subsequent processes are executed in the order of their arrival.

2. Round Robin:
Round Robin is a preemptive scheduling algorithm where each process is assigned a fixed time quantum to execute. Once a process's time quantum expires, it is preempted and added back to the end of the ready queue.

3. Shortest Remaining Time First (SRTF):
This strategy selects the process with the shortest remaining burst time to execute next. It is a preemptive scheduling algorithm.

4. Custom algorithm: This is a preemptive scheduling algorithm we customized, where processes are prioritized based on their process IDs. Even IDs are executed first, followed by odd IDs.
   
Instructions:
Our project code was implemented and executed using PyCharm. Any Python compiler can be used to run our code. 
Simply compile and execute the files named finalCode.py and Custom.py

Note: Make sure that the input file is named "processes.txt" and is located in the same path as the Python files.

1. Download the finalCode.py file, Custom.py file, and processes.txt (these files must be in the same path).
2. The FCFS, Round Robin, and SRTF functions are in the finalCode.py file; run the program to see the result.
3. If you want to change the input file, go to the main part and change the content of p_file.
4. To use the custom function, run the custom.py file.
    
