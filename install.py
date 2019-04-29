# Run with sudo mode

import subprocess

# apply xonsh profiles
subprocess.run(['cp', './.xonshrc', '~/'])
subprocess.run(['/usr/bin/env', 'xonsh', '-c', '~/.xonshrc'])

# Install VSCode extensions
with open('extensions') as f:
    extensions = f.read().split('\n')
    for extension in extensions:
        subprocess.run(['code', '--install-extension', extension])
