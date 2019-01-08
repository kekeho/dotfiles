import subprocess

with open('extent') as f:
    extensions = f.read().split('\n')
    for extension in extensions:
        subprocess.run(['code', '--install-extension', extension])
