
import shlex
import subprocess

class PyExecCmd(object):
    """
    Helper class to run a complex command through Python subprocess
    """
    def __init__(self):
        return

    def exec_cmd(self, cmdstr, *args, **kwargs):
        """ *Safely* execute the command passed as the string using 
            Popen invocation without shell=True. The command may contain 
            multiple piped commands. Returns the <stdout> and <stderr> of 
            executing the command.
            Args:
                @param cmdstr:      type string
            Returns:
                tuple
        """
        allcmds = cmdstr.split('|')
        numcmds = len(allcmds)

        popen_objs = []
        for i in range(numcmds):
            scmd = shlex.split(allcmds[i])
            stdin = None if i == 0 else popen_objs[i-1].stdout
            stderr = subprocess.STDOUT if i < (numcmds - 1) else subprocess.PIPE

            thiscmd_p = subprocess.Popen(scmd, stdin=stdin,
                                         stdout=subprocess.PIPE,
                                         stderr=stderr, *args, **kwargs)
            if i != 0: popen_objs[i-1].stdout.close()
            popen_objs.append(thiscmd_p)

        # Collect output from the final command
        (cmdout, cmderr) = popen_objs[-1].communicate()

        # Set return codes
        for i in range(len(popen_objs) - 1):
            popen_objs[i].wait()

        # Now check if any command failed
        for i in range(numcmds):
            if popen_objs[i].returncode:
                raise subprocess.CalledProcessError(popen_objs[i].returncode,
                                                    allcmds[i])

        # All commands succeeded
        return (cmdout, cmderr)
		

if __name__ == '__main__':
	
	p = PyExecCmd()
	cmd = "echo file.txt | xargs -I FILE cat FILE"
	out, err = p.exec_cmd(cmd)
	print(out)
