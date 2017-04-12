import subprocess

# before this make sure you install pip3 and pyinstaller with pip3
# or else the the compile executable wont run
# see for output in the debugger and build in dist folder
subprocess.call('pyinstaller --windowed PythonImaging.py', shell=True)
