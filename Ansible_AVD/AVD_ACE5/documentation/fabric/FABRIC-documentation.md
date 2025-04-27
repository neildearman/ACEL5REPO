# FABRIC

## Table of Contents

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| FABRIC | l3leaf | borderleaf1 | 192.168.0.25/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | borderleaf2 | 192.168.0.26/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf1 | 192.168.0.21/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf2 | 192.168.0.22/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf3 | 192.168.0.23/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf4 | 192.168.0.24/24 | cEOS-lab | Provisioned | - |
| FABRIC | spine | spine1 | 192.168.0.11/24 | cEOS-lab | Provisioned | - |
| FABRIC | spine | spine2 | 192.168.0.12/24 | cEOS-lab | Provisioned | - |
| FABRIC | spine | spine3 | 192.168.0.13/24 | cEOS-lab | Provisioned | - |
| FABRIC | spine | spine4 | 192.168.0.14/24 | cEOS-lab | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | borderleaf1 | Ethernet1 | mlag_peer | borderleaf2 | Ethernet1 |
| l3leaf | borderleaf1 | Ethernet2 | mlag_peer | borderleaf2 | Ethernet2 |
| l3leaf | borderleaf1 | Ethernet3 | spine | spine1 | Ethernet7 |
| l3leaf | borderleaf1 | Ethernet4 | spine | spine2 | Ethernet7 |
| l3leaf | borderleaf1 | Ethernet5 | spine | spine3 | Ethernet7 |
| l3leaf | borderleaf1 | Ethernet6 | spine | spine4 | Ethernet7 |
| l3leaf | borderleaf2 | Ethernet3 | spine | spine1 | Ethernet8 |
| l3leaf | borderleaf2 | Ethernet4 | spine | spine2 | Ethernet8 |
| l3leaf | borderleaf2 | Ethernet5 | spine | spine3 | Ethernet8 |
| l3leaf | borderleaf2 | Ethernet6 | spine | spine4 | Ethernet8 |
| l3leaf | leaf1 | Ethernet1 | mlag_peer | leaf2 | Ethernet1 |
| l3leaf | leaf1 | Ethernet2 | mlag_peer | leaf2 | Ethernet2 |
| l3leaf | leaf1 | Ethernet3 | spine | spine1 | Ethernet3 |
| l3leaf | leaf1 | Ethernet4 | spine | spine2 | Ethernet3 |
| l3leaf | leaf1 | Ethernet5 | spine | spine3 | Ethernet3 |
| l3leaf | leaf1 | Ethernet6 | spine | spine4 | Ethernet3 |
| l3leaf | leaf2 | Ethernet3 | spine | spine1 | Ethernet4 |
| l3leaf | leaf2 | Ethernet4 | spine | spine2 | Ethernet4 |
| l3leaf | leaf2 | Ethernet5 | spine | spine3 | Ethernet4 |
| l3leaf | leaf2 | Ethernet6 | spine | spine4 | Ethernet4 |
| l3leaf | leaf3 | Ethernet3 | spine | spine1 | Ethernet5 |
| l3leaf | leaf3 | Ethernet4 | spine | spine2 | Ethernet5 |
| l3leaf | leaf3 | Ethernet5 | spine | spine3 | Ethernet5 |
| l3leaf | leaf3 | Ethernet6 | spine | spine4 | Ethernet5 |
| l3leaf | leaf4 | Ethernet3 | spine | spine1 | Ethernet6 |
| l3leaf | leaf4 | Ethernet4 | spine | spine2 | Ethernet6 |
| l3leaf | leaf4 | Ethernet5 | spine | spine3 | Ethernet6 |
| l3leaf | leaf4 | Ethernet6 | spine | spine4 | Ethernet6 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 10.10.1.0/24 | 256 | 48 | 18.75 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| borderleaf1 | Ethernet3 | 10.10.1.33/31 | spine1 | Ethernet7 | 10.10.1.32/31 |
| borderleaf1 | Ethernet4 | 10.10.1.35/31 | spine2 | Ethernet7 | 10.10.1.34/31 |
| borderleaf1 | Ethernet5 | 10.10.1.37/31 | spine3 | Ethernet7 | 10.10.1.36/31 |
| borderleaf1 | Ethernet6 | 10.10.1.39/31 | spine4 | Ethernet7 | 10.10.1.38/31 |
| borderleaf2 | Ethernet3 | 10.10.1.41/31 | spine1 | Ethernet8 | 10.10.1.40/31 |
| borderleaf2 | Ethernet4 | 10.10.1.43/31 | spine2 | Ethernet8 | 10.10.1.42/31 |
| borderleaf2 | Ethernet5 | 10.10.1.45/31 | spine3 | Ethernet8 | 10.10.1.44/31 |
| borderleaf2 | Ethernet6 | 10.10.1.47/31 | spine4 | Ethernet8 | 10.10.1.46/31 |
| leaf1 | Ethernet3 | 10.10.1.1/31 | spine1 | Ethernet3 | 10.10.1.0/31 |
| leaf1 | Ethernet4 | 10.10.1.3/31 | spine2 | Ethernet3 | 10.10.1.2/31 |
| leaf1 | Ethernet5 | 10.10.1.5/31 | spine3 | Ethernet3 | 10.10.1.4/31 |
| leaf1 | Ethernet6 | 10.10.1.7/31 | spine4 | Ethernet3 | 10.10.1.6/31 |
| leaf2 | Ethernet3 | 10.10.1.9/31 | spine1 | Ethernet4 | 10.10.1.8/31 |
| leaf2 | Ethernet4 | 10.10.1.11/31 | spine2 | Ethernet4 | 10.10.1.10/31 |
| leaf2 | Ethernet5 | 10.10.1.13/31 | spine3 | Ethernet4 | 10.10.1.12/31 |
| leaf2 | Ethernet6 | 10.10.1.15/31 | spine4 | Ethernet4 | 10.10.1.14/31 |
| leaf3 | Ethernet3 | 10.10.1.17/31 | spine1 | Ethernet5 | 10.10.1.16/31 |
| leaf3 | Ethernet4 | 10.10.1.19/31 | spine2 | Ethernet5 | 10.10.1.18/31 |
| leaf3 | Ethernet5 | 10.10.1.21/31 | spine3 | Ethernet5 | 10.10.1.20/31 |
| leaf3 | Ethernet6 | 10.10.1.23/31 | spine4 | Ethernet5 | 10.10.1.22/31 |
| leaf4 | Ethernet3 | 10.10.1.25/31 | spine1 | Ethernet6 | 10.10.1.24/31 |
| leaf4 | Ethernet4 | 10.10.1.27/31 | spine2 | Ethernet6 | 10.10.1.26/31 |
| leaf4 | Ethernet5 | 10.10.1.29/31 | spine3 | Ethernet6 | 10.10.1.28/31 |
| leaf4 | Ethernet6 | 10.10.1.31/31 | spine4 | Ethernet6 | 10.10.1.30/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 172.16.0.71/28 | 16 | 6 | 37.5 % |
| 172.16.0.101/28 | 16 | 4 | 25.0 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| FABRIC | borderleaf1 | 172.16.0.69/32 |
| FABRIC | borderleaf2 | 172.16.0.70/32 |
| FABRIC | leaf1 | 172.16.0.65/32 |
| FABRIC | leaf2 | 172.16.0.66/32 |
| FABRIC | leaf3 | 172.16.0.67/32 |
| FABRIC | leaf4 | 172.16.0.68/32 |
| FABRIC | spine1 | 172.16.0.107/32 |
| FABRIC | spine2 | 172.16.0.108/32 |
| FABRIC | spine3 | 172.16.0.109/32 |
| FABRIC | spine4 | 172.16.0.110/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 172.16.1.70/28 | 16 | 6 | 37.5 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| FABRIC | borderleaf1 | 172.16.1.69/32 |
| FABRIC | borderleaf2 | 172.16.1.69/32 |
| FABRIC | leaf1 | 172.16.1.65/32 |
| FABRIC | leaf2 | 172.16.1.65/32 |
| FABRIC | leaf3 | 172.16.1.67/32 |
| FABRIC | leaf4 | 172.16.1.68/32 |
