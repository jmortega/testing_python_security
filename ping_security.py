import subprocess

#the problem is that the shell can process other commands that are provided by the user after the ping command terminates.
def ping_unsafe(myserver):
    return subprocess.Popen('ping -c 1 %s' % myserver, shell=True)

#Rather than passing a string to subprocess, our function passes a list of strings. 
#The ping program gets each argument separately, 
#so the shell does not process other commands that are provided by the user after the ping command terminates.

def ping_safe(myserver):
    args = ['ping','-c','1', myserver]
    return subprocess.Popen(args, shell=False)
	
#print(ping_unsafe('8.8.8.8 & touch file'))

print(ping_safe('8.8.8.8'))