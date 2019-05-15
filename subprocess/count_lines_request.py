import subprocess

#The function is insecure because it uses shell=True, which allows shell injection. 
#A user to who instructs your code to fetch the website ; rm -rf / can do terrible things to what used to be your machine.

def count_lines_unsafe(website):
    return subprocess.check_output('curl %s | wc -l' % website, shell=True)

#Rather than calling a single shell process that runs each of our programs, 
#we run them separately and connect stdout from curl to stdin for wc. 
#We specify stdout=subprocess.PIPE, which tells subprocess to send that output to the respective file handler.

def count_lines_safe(website):
    args = ['curl', website]
    args2 = ['wc', '-l']
    process_curl = subprocess.Popen(args, stdout=subprocess.PIPE,
                                    shell=False)
    process_wc = subprocess.Popen(args2, stdin=process_curl.stdout,
                                  stdout=subprocess.PIPE, shell=False)
    # Allow process_curl to receive a SIGPIPE if process_wc exits.
    process_curl.stdout.close()
    return process_wc.communicate()[0]
	
print(count_lines_unsafe('www.google.com & touch file'))