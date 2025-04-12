import pyeapi
import yaml

file = open('vlans.yml','r')
vlan_file_dict = yaml.safe_load(file)

pyeapi.load_config('eapi.conf')

for switch in vlan_file_dict['switches']:
    connect = pyeapi.connect_to(switch)
    raw_cmd_result = connect.enable('show vlan')
    cmd_vlan_dict = (raw_cmd_result[0]['result']['vlans'])
    print(f'For switch {switch}')
    for vlan in cmd_vlan_dict:
        vlan_id = vlan
        vlan_name = (cmd_vlan_dict[vlan]['name'])
        print(f'VLAN ID of {vlan_id}, with name {vlan_name}')


  
    
    