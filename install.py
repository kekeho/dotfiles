# Run with sudo mode

import subprocess
import shutil
import os
import platform

# if Linux, install mackeyX
if platform.system() == 'Linux':
    subprocess.run(['git', 'clone', 'https://github.com/kekeho/mackeyX.git'])
    subprocess.run(['sh', 'mackeyX/set.sh'], shell=True)

# apply xonsh profiles
shutil.copy('.xonshrc', f'{os.environ["HOME"]}/.xonshrc')
subprocess.run(['/usr/bin/env', 'xonsh', '-c', '~/.xonshrc'])

# Install VSCode extensions
with open('extensions') as f:
    extensions = f.read().split('\n')
    for extension in extensions:
        subprocess.run(['code', '--install-extension', extension])
