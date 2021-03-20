# utils.py

from subprocess import Popen, PIPE, TimeoutExpired

def exec_cmd(cmd, cmd_input = "", cmd_timeout = None):
    prosses = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    (stdout, stderr) = ("", "")
    timeout_flag = 0

    try:
        (stdout, stderr) = prosses.communicate(input=cmd_input, timeout=cmd_timeout)
    except TimeoutExpired:
        prosses.kill()
        (stdout, stderr) = prosses.communicate()
        timeout_flag = 1

    exit_code = int(prosses.wait())
    return (cmd_input, stdout.decode(), stderr.decode(), exit_code, timeout_flag)
