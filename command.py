'''
Name: Joshua Riley
Python Intern Assignment 2

'''

#import Popen module
import subprocess 
#import time module
import time
#import timeit module
import timeit
#import process_tune module directly from time module
from time import process_time #Python version 3.3

#list of commands 
commands = [
    'sleep 3',
    'ls -l /',
    'find /',
    'sleep 4',
    'find /usr',
    'date',
    'sleep 5',
    'uptime'
]

#initialize time-keepers
total_elapsed = 0
total_exec = 0
average_exec = 0
minimum_exec = 0
maximum_exec = 0
exec_list = [] 

#execute the commands
for command in commands:
    start_time = timeit.default_timer()
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    start_exec = process_time()
    print(command)
    print('----------')
    #process still running
    while process.poll() is None: #process is running
        process.communicate() #reads input until process is finished   
    print("Process exit return code:", process.returncode) #process finished running
    print('\n')
    end_time = timeit.default_timer()
    elapsed_time = end_time - start_time #seconds
    total_elapsed = total_elapsed + elapsed_time
    exec_time = process_time() - start_exec #fractional seconds
    total_exec = total_exec + exec_time  
    exec_list.append(exec_time) #append execution time to the list

#average execution time
average_exec = total_exec / len(commands)

#minimum execution time
minimum_exec = min(exec_list) 

#maximum execution time
maximum_exec = max(exec_list)

#generate  report
print("Report")
print('----------')
print("total elapsed time:", total_elapsed)
print("average execution time:", average_exec)
print("minimum execution time:", minimum_exec)
print("maximum execution time:", maximum_exec)

    