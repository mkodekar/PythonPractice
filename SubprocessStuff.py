import subprocess

# for windows subprocess.call('dir', shell=True)
subprocess.call('ls', shell=True)

output = subprocess.check_output('ls', shell=True)
print('Output is', output)

# calling the system library
subprocess.call('python3 TheSystemLibrary.py "Hey there !"', shell=True)

#with output
output2 = subprocess.check_output('python3 TheSystemLibrary.py "Hey there !"', shell=True)
print(output2)

# installing modules from the subprocess #which gives me error in the
# pycharm ide saying no tty present and no
# askpass program specified
subprocess.call('sudo apt-get install python3-tweepy', shell=True)
