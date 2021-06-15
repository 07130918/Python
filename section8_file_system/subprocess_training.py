import subprocess

r = subprocess.run(['ls', '-l'])
# 非推奨
# subprocess.run('ls -l | grep test', shell=True)
print(r.returncode)
