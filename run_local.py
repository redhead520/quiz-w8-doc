import os

print('current working dir [{0}]'.format(os.getcwd()))
w_d = os.path.dirname(os.path.abspath(__file__))
print('change wording dir to [{0}]'.format(w_d))
os.chdir(w_d)
command = '/bin/bash -c "cd {0} && source ./run_local.sh"'.format(w_d)
for l in os.popen(command):
    print(l.strip())
