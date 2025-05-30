import pyeapi
import os
import yaml

pyeapi.load_config('eapi.conf')

file = open('vlans.yml','r')

switch_dict = yaml.safe_load(file)

# for switch in switch_dict['switches']:
#     print(switch)

directory = "configs"
exists = os.path.exists(directory)
if not exists:
    os.makedirs(directory)

# # # switches = ['leaf1', 'leaf2', 'leaf3', 'leaf4', 'spine1', 'spine2', 'spine3', 'spine4', 'borderleaf1', 'borderleaf2']

for switch in switch_dict['switches']:
    connect = pyeapi.connect_to(switch)
    running_config = connect.get_config(as_string='True')
    path = directory+'/'+switch+'.cfg'
    file = open(path,'w')
    file.write(running_config)
    file.close()
    print(f"Backing up {switch}")



 

