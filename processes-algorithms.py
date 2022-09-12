process_name = 'ProcessName'

burst_time = 'BrustTime'

arrival_time = 'ArrivalTime'

start_time = 'StartTime'

waitting_time = 'Waitingtime'

p1 = {
    process_name : "P1",
    burst_time : 6,
    arrival_time : 2
}

p2 = {
    process_name : "P2",
    burst_time : 2,
    arrival_time : 5
}

p3 = {
    process_name : "P3",
    burst_time : 8,
    arrival_time : 1
}

p4 = {
    process_name : "P4",
    burst_time : 3,
    arrival_time : 0
}

p5 = {
    process_name : "P5",
    burst_time : 4,
    arrival_time : 4
}

processes = [p1, p2, p3, p4, p5]

def fcfs(processes : list):
    num_of_processes = len(processes)
    processes.sort(key=lambda x : x[arrival_time])

    time = 0
    time_wait_sum = 0

    while processes:
        exec_prcs = processes.pop(0)

        if time < exec_prcs[arrival_time]:
            exec_prcs[start_time] = time + exec_prcs[arrival_time]
        else:
            exec_prcs[start_time] = time

        time += exec_prcs[burst_time]

        print("Process name: ", exec_prcs[process_name])

        wait_time = exec_prcs[start_time] - exec_prcs[arrival_time]

        exec_prcs[waitting_time] = wait_time
        time_wait_sum += wait_time

        print("Waiting time: ", str(wait_time))
        print('-'*10)

    print('Average Waiting Time: ', str(time_wait_sum/num_of_processes))

#fcfs(processes)


def p_sjf(processes : list):
    num_of_processes = len(processes)
    processes.sort(key=lambda x : x[arrival_time])    

    time = 0
    time_wait_sum = 0
    while processes:
        exec_prcs = processes.pop(0)

        if time < exec_prcs[arrival_time]:
            exec_prcs[start_time] = time + exec_prcs[arrival_time]
        else:
            exec_prcs[start_time] = time

        time += exec_prcs[burst_time]

        print("Process name: ", exec_prcs[process_name])

        wait_time = exec_prcs[start_time] - exec_prcs[arrival_time]

        exec_prcs[waitting_time] = wait_time
        time_wait_sum += wait_time

        print("Waiting time: ", str(wait_time))
        print('-'*10)

        processes.sort(key=lambda  x : x[burst_time])

    print('Average Waiting Time: ', str(time_wait_sum/num_of_processes))


p_sjf(processes)

