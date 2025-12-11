import subprocess
print(len(subprocess.check_output(f"factor {input()}", shell=True).split()))