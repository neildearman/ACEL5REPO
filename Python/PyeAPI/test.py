import pyeapi
import yaml

file = open('vlans.yml','r')

vlan_dict = yaml.safe_load(file)

pyeapi.load_config('eapi.conf')

# print(vlan_dict['vlans'][0]['name'])


# for switch in vlan_dict['switches']:
#     print(f'Switch {switch} has the following VLANS:')

#     for item in vlan_dict['vlans']:
#         print(item['name'])

for switch in vlan_dict['switches']:
    connect = pyeapi.connect_to(switch)
    print (f'Connecting to {switch}')
    for vlan in vlan_dict['vlans']: 
        vlan_id = vlan['id']
        vlan_name = vlan['name']
        print(f'Creating vlan {vlan_name}, with ID, {vlan_id}')
        vlan_api.create(vlan_id)
        vlan_api.set_name(vlan_id, vlan_name)
