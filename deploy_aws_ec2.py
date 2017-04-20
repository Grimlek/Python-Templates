import os
import re

# Find desired files for deployment
files = []
for file in os.listdir("directory_to_files_for_deployment"):
    if file.endswith(".jar"): # file extension that the files end with
        jar_files.append(file)

# Get the version numbers for each file and save to a list
versions = []
for file in files:
    version = re.findall(r'\d+', file)
    versions.append(''.join(version))

# Find the highest file version and get the index
max_file_version = max(versions)
max_index = versions.index(max_file_version)

# Deploy to aws
os.system("scp -i aws_public_key.pem directory_to_files_for_deployment_with_slash_at_end" + files[max_index] + " ec2-user@ec2_instance:")