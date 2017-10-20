from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('praktyka.py', base=base)
]

setup(name='Praktyka',
      version = '0.1',
      description = 'This app show Symbol statitics',
      options = dict(build_exe = buildOptions),
      executables = executables)
