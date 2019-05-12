# Run with sudo mode

import subprocess
import shutil
import os
import platform

OSNAME = platform.system()
PWD = os.path.abspath('.')

# if Linux, install mackeyX
if OSNAME == 'Linux':
    subprocess.run(['git', 'clone', 'https://github.com/kekeho/mackeyX.git'])
    subprocess.run(['sh', 'mackeyX/set.sh'], shell=True)

# apply xonsh profiles
shutil.copy('.xonshrc', f'{os.environ["HOME"]}/.xonshrc')
subprocess.run(['/usr/bin/env', 'xonsh', '-c', '~/.xonshrc'])

# apply vscode setting
if OSNAME == 'Linux':
    shutil.copy(f'{PWD}/vscode/settings.json', f'{os.environ["HOME"]}/.config/Code/User/settings.json')
elif OSNAME == 'Darwin':
    shutil.copy(f'{PWD}/vscode/settings.json', f'{os.environ["HOME"]}/Library/Application Support/Code/User/settings.json')

# Install VSCode extensions
with open(f'{PWD}/vscode/extensions') as f:
    extensions = f.read().split('\n')
    for extension in extensions:
        subprocess.run(['code', '--install-extension', extension])
