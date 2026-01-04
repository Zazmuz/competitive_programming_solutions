import subprocess
res = subprocess.check_output(f"factor {input()}", shell=True).split()[1:]
res = [x.decode() for x in res]
print(res[-1])