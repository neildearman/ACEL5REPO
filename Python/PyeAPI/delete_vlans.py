import yaml
import pyeapi

def load_switches_from_yaml(filename):
    """Load switches connection info from a YAML file."""
    with open(filename, 'r') as file:
        config = yaml.safe_load(file)
    return config.get('switches', [])

def read_vlans_from_file(filename):
    """Reads VLAN IDs from a file."""
    with open(filename, 'r') as file:
        vlans = [line.strip() for line in file if line.strip()]
    return vlans

def connect_to_switch(switch_info):
    """Connects to a switch using pyeapi."""
    return pyeapi.client.connect(
        transport=switch_info.get('transport', 'https'),
        host=switch_info['host'],
        username=switch_info['username'],
        password=switch_info['password'],
        port=443
    )

def delete_vlans_from_device(node, vlans, switch_name):
    """Deletes VLANs from a given device."""
    device = pyeapi.client.Node(node)
    for vlan in vlans:
        command = f'no vlan {vlan}'
        print(f"[{switch_name}] Deleting VLAN {vlan}")
        device.config([command])

def main():
    yaml_file = 'eapi.yml'
    vlan_file = 'vlans.txt'

    switches = load_switches_from_yaml(yaml_file)
    vlans = read_vlans_from_file(vlan_file)

    if not switches:
        print("No switches found in YAML configuration.")
        return
    if not vlans:
        print("No VLANs found to delete.")
        return

    for switch in switches:
        try:
            print(f"\nConnecting to {switch['name']} ({switch['host']})...")
            node = connect_to_switch(switch)
            delete_vlans_from_device(node, vlans, switch['name'])
        except Exception as e:
            print(f"Failed to process {switch['name']}: {e}")

if __name__ == "__main__":
    main()
