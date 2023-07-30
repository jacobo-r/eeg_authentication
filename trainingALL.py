import yaml
import os
import shutil
import subprocess

# The configuration file path
config_file_path = '../config/mixed_fbcnet_config.yaml'
# Path to main.py script
main_script_path = './main.py'

l=[1,3,6,8,9,10]

for subject_num in l:
    # Open the YAML file and load its content
    with open(config_file_path, 'r') as file:
        config = yaml.safe_load(file)
    
    # Change the subject number
    config['train']['subject'] = subject_num

    # Write the new configuration to a temporary YAML file
    temp_config_file = '../config/temp_config.yaml'
    with open(temp_config_file, 'w') as file:
        yaml.dump(config, file)

    # Execute main.py with the new configuration
    subprocess.run(['python', main_script_path, temp_config_file])

    # Delete the temporary file
    os.remove(temp_config_file)
