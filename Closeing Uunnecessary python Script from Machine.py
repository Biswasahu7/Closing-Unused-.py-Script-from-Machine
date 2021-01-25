#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing libraries
import subprocess
import os
import datetime
import signal


# In[2]:


def list_command(args='-ef'):
    
    # the ls ubuntu command
    cmd = 'ps'
    
    # using the Popen function to execute the command and store the result in temp.
    # it returns a tuple that contains the data and the error if any.
    temp = subprocess.Popen([cmd,args], stdout=subprocess.PIPE)
    
    # we use the communicate function to fetch the output
    output = str(temp.communicate())
    
    #splitting the output so that we can parse them line by line
    output = output.split("\n")
    output = output[0].split('\\')
    
     # a variable to store the output
    res = []
    
    # iterate through the output line by line
    for line in output:
        res.append(line)
        
    # print the output
    py=[]
    
    for i in range(1, len(res) - 1):
        if "/usr/bin/python3.8" in res[i]:
            temp=res[i].split()
            py.append(temp)
            
        # if "check_python_processes.py" in res[i]: print("ITS PYTHON PROCESS RUNNING...")
        print(res[i])
     #Printing python script   
    print("Its python scripts - {}-{}".format(len(py),py))
    
    #Assigning pid empty list to append other python script to kill
    pid=[]
    
    #Running for loop into py list to varifiy our required python script which is running
    for p in py:
        
        #If our required python script is the no matching then append the script to pid list
        if "/home/server/OCR/check_python_processes.py" not in p:
            pid.append(p[1])
    
    #After appending all unnecessary python script kill all
    print("Kill PIDs-{}".format(pid))
    
    
    if len(pid)>0:
        for p in pid:
            os.kill(int(p), signal.SIGTERM)  # or signal.SIGKILL
    print("DONE...")
    
    return res

#list_command()


# In[ ]:




