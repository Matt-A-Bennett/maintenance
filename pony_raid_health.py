import subprocess

subprocess
query = subprocess.run(['ssh', 'mbennett@storage.cism.ucl.ac.be', 'sudo /usr/sbin/storcli show all'], stdout=subprocess.PIPE).stdout.decode('utf-8')
print(query)
