import subprocess

with open('extensions') as f:
    extensions = f.read().split('\n')
    for extension in extensions:
        subprocess.run(['code', '--install-extension', extension])
