#!/usr/bin/env python3

import subprocess
import os

vcpkg = os.path.join(os.path.dirname(__file__), 'vcpkg')

# in dependency order
packages = [ 
    'results',
    'kb64',
    'composite',
    'krc',

    'kyaml',
    'kthread',

    'klog',
]

def banner(msg):
    print('*' * len(msg))
    print(msg)
    print('*' * len(msg))

for package in reversed(packages):
    banner(f'removing {package}')
    subprocess.check_call([vcpkg, 'remove', package])

for package in packages:
    banner(f'installing {package}')
    subprocess.check_call([vcpkg, 'install', '--head', package])

banner('done')
