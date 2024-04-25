import os
import json
import subprocess
import sys

directory_name = sys.argv[1]

directory = f"/home/codevuln/target-repo/{directory_name}/semgrep"
output_filename = "semgrep.json"
data = {}

for i, filename in enumerate(os.listdir(directory), start=1):
    if filename.endswith('.json'):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r') as f:
            file_data = json.load(f)  
            data[filename] = file_data  

with open(os.path.join(directory, output_filename), 'w') as f:
    json.dump(data, f, indent=4)

print(f"All JSON files have been merged into {output_filename} in the directory {directory}.")

subprocess.run(['jq', '.', 'semgrep.json'], stdout=open('semgrep.json', 'w'))

import os
import json
import subprocess
import sys

directory_name = sys.argv[1]

directory = f"/home/codevuln/target-repo/{directory_name}/semgrep"
output_filename = "semgrep.json"
data = {}

for i, filename in enumerate(os.listdir(directory), start=1):
    if filename.endswith('.json'):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r') as f:
            file_data = json.load(f)  
            data[filename] = file_data  

with open(os.path.join(directory, output_filename), 'w') as f:
    json.dump(data, f, indent=4)

print(f"All JSON files have been merged into {output_filename} in the directory {directory}.")

subprocess.run(['jq', '.', 'semgrep.json'], stdout=open('semgrep.json', 'w'))

delete_command = f"mv /home/codevuln/target-repo/{directory_name}/semgrep/semgrep.json /home/codevuln && rm -rf /home/codevuln/target-repo/{directory_name}/semgrep/*.json && mv /home/codevuln/semgrep.json /home/codevuln/target-repo/{directory_name}/semgrep/semgrep.json"
subprocess.run(delete_command, shell=True, check=True, cwd = f"/home/codevuln/target-repo/{directory_name}/semgrep/")