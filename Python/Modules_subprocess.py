import subprocess

cmd='df -h;pwd'
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
print(p.stdout.read())
