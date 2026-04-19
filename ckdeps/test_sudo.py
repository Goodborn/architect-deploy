import subprocess
p = subprocess.Popen(['sudo', '-S', 'pacman', '-Syu', '--noconfirm'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
p.stdin.write("badpassword\n")
p.stdin.flush()
for line in p.stdout:
    print(line, end='')
p.wait()
