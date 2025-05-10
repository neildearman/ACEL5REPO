import pyeapi
import yaml

file = open('vlans.yml','r')

vlan_dict = yaml.safe_load(file)

pyeapi.load_config('eapi.conf')

# print(vlan_dict['vlans'][0]['name'])
# print (vlan_dict['switches']['leaf1']['staticroutes']['destination'])
# print (vlan_dict['switches']['leaf1']['staticroutes']['next_hop'])

for switch in vlan_dict['switches']:
    print(f'Switch {switch} has the following VLANS:')

    for item in vlan_dict['vlans']:
        print(item['name'])

for switch in vlan_dict['switches']:
    connect = pyeapi.connect_to(switch)
    print (f'Connecting to {switch}')
    for vlan in vlan_dict['vlans']: 
        vlan_api = connect.api('vlans')
        vlan_id = vlan['id']
        vlan_name = vlan['name']
        print(f'Creating vlan {vlan_name}, with ID, {vlan_id}')
        vlan_api.create(vlan_id)
        vlan_api.set_name(vlan_id, vlan_name)

for switch in vlan_dict['switches']:
    connect = pyeapi.connect_to(switch)
    print(f"Connected to {switch}")
    for route in vlan_dict['switches'][switch]['staticroutes']:
        staticroute_api = connect.api('staticroute')               
        destination = route['destination']
        next_hop = route['next_hop']
        print(f"Creating static route {destination} with next hop {next_hop}")
        staticroute_api.create(destination, next_hop)
    print(f"Static route {destination} created with next hop {next_hop} on {switch}")
        
for switch in vlan_dict['switches']:
    connect = pyeapi.connect_to(switch)
    print (f'Connecting to {switch}')
    stp_api = connect.api('stp')
    stp_api.set_mode('mstp')
    print(f"STP mode set to MSTP on {switch}")
