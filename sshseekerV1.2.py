#!/usr/bin/env python3
'''
	sshseekerV1.py
	SSH seeker!
	1 to 65535 ports 
	over just one IP host.

'''
import subprocess
import sys

HOST="192.168.0.1"

for port in range(1, 65535):
	COMMAND="-p "
	COMMAND+=str(port)
	ssh = subprocess.Popen(["ssh", HOST, COMMAND],
	                       shell=False,
	                       stdout=subprocess.PIPE,
	                       stderr=subprocess.PIPE)
	result = ssh.stdout.readlines()
	if result == []:
		print("Invalid port number: ", port)
		pass
	else:
		print (result)