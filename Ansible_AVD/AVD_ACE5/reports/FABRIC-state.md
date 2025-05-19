
# Validate State Report

**Table of Contents:**

- [Validate State Report](validate-state-report)
  - [Test Results Summary](#test-results-summary)
  - [Failed Test Results Summary](#failed-test-results-summary)
  - [All Test Results](#all-test-results)

## Test Results Summary

### Summary Totals

| Total Tests | Total Tests Passed | Total Tests Failed |
| ----------- | ------------------ | ------------------ |
| 488 | 484 | 4 |

### Summary Totals Devices Under Tests

| DUT | Total Tests | Tests Passed | Tests Failed | Categories Failed |
| --- | ----------- | ------------ | ------------ | ----------------- |
| borderleaf1 |  58 | 57 | 1 | Interface State |
| borderleaf2 |  58 | 57 | 1 | Interface State |
| leaf1 |  65 | 64 | 1 | Interface State |
| leaf2 |  65 | 64 | 1 | Interface State |
| leaf3 |  55 | 55 | 0 | - |
| leaf4 |  55 | 55 | 0 | - |
| spine1 |  33 | 33 | 0 | - |
| spine2 |  33 | 33 | 0 | - |
| spine3 |  33 | 33 | 0 | - |
| spine4 |  33 | 33 | 0 | - |

### Summary Totals Per Category

| Test Category | Total Tests | Tests Passed | Tests Failed |
| ------------- | ----------- | ------------ | ------------ |
| NTP |  10 | 10 | 0 |
| Interface State |  116 | 112 | 4 |
| LLDP Topology |  56 | 56 | 0 |
| MLAG |  4 | 4 | 0 |
| IP Reachability |  48 | 48 | 0 |
| BGP |  110 | 110 | 0 |
| Routing Table |  84 | 84 | 0 |
| Loopback0 Reachability |  60 | 60 | 0 |

## Failed Test Results Summary

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |
| 79 | leaf1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel9 - host2_PortChannel host2 | FAIL | Interface shutdown: False - interface status: down - line protocol status: lowerLayerDown |
| 82 | leaf2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel9 - host2_PortChannel host2 | FAIL | Interface shutdown: False - interface status: down - line protocol status: lowerLayerDown |
| 105 | borderleaf1 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | FAIL | Interface status: down - line protocol status: down |
| 106 | borderleaf2 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | FAIL | Interface status: down - line protocol status: down |

## All Test Results

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |
| 1 | borderleaf1 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 2 | borderleaf2 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 3 | leaf1 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 4 | leaf2 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 5 | leaf3 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 6 | leaf4 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 7 | spine1 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 8 | spine2 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 9 | spine3 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 10 | spine4 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 11 | borderleaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - MLAG_PEER_borderleaf2_Ethernet1 | PASS | - |
| 12 | borderleaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - MLAG_PEER_borderleaf2_Ethernet2 | PASS | - |
| 13 | borderleaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1_Ethernet7 | PASS | - |
| 14 | borderleaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2_Ethernet7 | PASS | - |
| 15 | borderleaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3_Ethernet7 | PASS | - |
| 16 | borderleaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_SPINE4_Ethernet7 | PASS | - |
| 17 | borderleaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - MLAG_PEER_borderleaf1_Ethernet1 | PASS | - |
| 18 | borderleaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - MLAG_PEER_borderleaf1_Ethernet2 | PASS | - |
| 19 | borderleaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1_Ethernet8 | PASS | - |
| 20 | borderleaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2_Ethernet8 | PASS | - |
| 21 | borderleaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3_Ethernet8 | PASS | - |
| 22 | borderleaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_SPINE4_Ethernet8 | PASS | - |
| 23 | leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - MLAG_PEER_leaf2_Ethernet1 | PASS | - |
| 24 | leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - MLAG_PEER_leaf2_Ethernet2 | PASS | - |
| 25 | leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1_Ethernet3 | PASS | - |
| 26 | leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2_Ethernet3 | PASS | - |
| 27 | leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3_Ethernet3 | PASS | - |
| 28 | leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_SPINE4_Ethernet3 | PASS | - |
| 29 | leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - host1_Ethernet1 | PASS | - |
| 30 | leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet9 - host2_Ethernet1 | PASS | - |
| 31 | leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - MLAG_PEER_leaf1_Ethernet1 | PASS | - |
| 32 | leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - MLAG_PEER_leaf1_Ethernet2 | PASS | - |
| 33 | leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1_Ethernet4 | PASS | - |
| 34 | leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2_Ethernet4 | PASS | - |
| 35 | leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3_Ethernet4 | PASS | - |
| 36 | leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_SPINE4_Ethernet4 | PASS | - |
| 37 | leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - host1_Ethernet2 | PASS | - |
| 38 | leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet9 - host2_Ethernet2 | PASS | - |
| 39 | leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1_Ethernet5 | PASS | - |
| 40 | leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2_Ethernet5 | PASS | - |
| 41 | leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3_Ethernet5 | PASS | - |
| 42 | leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_SPINE4_Ethernet5 | PASS | - |
| 43 | leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - host3_Ethernet1 | PASS | - |
| 44 | leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet9 - host4_Ethernet1 | PASS | - |
| 45 | leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1_Ethernet6 | PASS | - |
| 46 | leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2_Ethernet6 | PASS | - |
| 47 | leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3_Ethernet6 | PASS | - |
| 48 | leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_SPINE4_Ethernet6 | PASS | - |
| 49 | leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - host3_Ethernet2 | PASS | - |
| 50 | leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet9 - host4_Ethernet2 | PASS | - |
| 51 | spine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_LEAF1_Ethernet3 | PASS | - |
| 52 | spine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_LEAF2_Ethernet3 | PASS | - |
| 53 | spine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_LEAF3_Ethernet3 | PASS | - |
| 54 | spine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_LEAF4_Ethernet3 | PASS | - |
| 55 | spine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - P2P_LINK_TO_BORDERLEAF1_Ethernet3 | PASS | - |
| 56 | spine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet8 - P2P_LINK_TO_BORDERLEAF2_Ethernet3 | PASS | - |
| 57 | spine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_LEAF1_Ethernet4 | PASS | - |
| 58 | spine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_LEAF2_Ethernet4 | PASS | - |
| 59 | spine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_LEAF3_Ethernet4 | PASS | - |
| 60 | spine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_LEAF4_Ethernet4 | PASS | - |
| 61 | spine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - P2P_LINK_TO_BORDERLEAF1_Ethernet4 | PASS | - |
| 62 | spine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet8 - P2P_LINK_TO_BORDERLEAF2_Ethernet4 | PASS | - |
| 63 | spine3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_LEAF1_Ethernet5 | PASS | - |
| 64 | spine3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_LEAF2_Ethernet5 | PASS | - |
| 65 | spine3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_LEAF3_Ethernet5 | PASS | - |
| 66 | spine3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_LEAF4_Ethernet5 | PASS | - |
| 67 | spine3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - P2P_LINK_TO_BORDERLEAF1_Ethernet5 | PASS | - |
| 68 | spine3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet8 - P2P_LINK_TO_BORDERLEAF2_Ethernet5 | PASS | - |
| 69 | spine4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_LEAF1_Ethernet6 | PASS | - |
| 70 | spine4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_LEAF2_Ethernet6 | PASS | - |
| 71 | spine4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_LEAF3_Ethernet6 | PASS | - |
| 72 | spine4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_LEAF4_Ethernet6 | PASS | - |
| 73 | spine4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - P2P_LINK_TO_BORDERLEAF1_Ethernet6 | PASS | - |
| 74 | spine4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet8 - P2P_LINK_TO_BORDERLEAF2_Ethernet6 | PASS | - |
| 75 | borderleaf1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel1 - MLAG_PEER_borderleaf2_Po1 | PASS | - |
| 76 | borderleaf2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel1 - MLAG_PEER_borderleaf1_Po1 | PASS | - |
| 77 | leaf1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel1 - MLAG_PEER_leaf2_Po1 | PASS | - |
| 78 | leaf1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel7 - host1_PortChannel host1 | PASS | - |
| 79 | leaf1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel9 - host2_PortChannel host2 | FAIL | Interface shutdown: False - interface status: down - line protocol status: lowerLayerDown |
| 80 | leaf2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel1 - MLAG_PEER_leaf1_Po1 | PASS | - |
| 81 | leaf2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel7 - host1_PortChannel host1 | PASS | - |
| 82 | leaf2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel9 - host2_PortChannel host2 | FAIL | Interface shutdown: False - interface status: down - line protocol status: lowerLayerDown |
| 83 | leaf3 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel7 - host3_PortChannel host3 | PASS | - |
| 84 | leaf3 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel9 - host4_PortChannel host4 | PASS | - |
| 85 | leaf4 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel7 - host3_PortChannel host3 | PASS | - |
| 86 | leaf4 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel9 - host4_PortChannel host4 | PASS | - |
| 87 | borderleaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 88 | borderleaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 89 | borderleaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 90 | borderleaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 91 | leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 92 | leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 93 | leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - VLAN10 | PASS | - |
| 94 | leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - VLAN20 | PASS | - |
| 95 | leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF_A | PASS | - |
| 96 | leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 97 | leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 98 | leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - VLAN10 | PASS | - |
| 99 | leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - VLAN20 | PASS | - |
| 100 | leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF_A | PASS | - |
| 101 | leaf3 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan30 - VLAN30 | PASS | - |
| 102 | leaf3 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan40 - VLAN40 | PASS | - |
| 103 | leaf4 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan30 - VLAN30 | PASS | - |
| 104 | leaf4 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan40 - VLAN40 | PASS | - |
| 105 | borderleaf1 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | FAIL | Interface status: down - line protocol status: down |
| 106 | borderleaf2 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | FAIL | Interface status: down - line protocol status: down |
| 107 | leaf1 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 108 | leaf2 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 109 | leaf3 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 110 | leaf4 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 111 | borderleaf1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 112 | borderleaf1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 113 | borderleaf2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 114 | borderleaf2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 115 | leaf1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 116 | leaf1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 117 | leaf2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 118 | leaf2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 119 | leaf3 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 120 | leaf3 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 121 | leaf4 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 122 | leaf4 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 123 | spine1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 124 | spine2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 125 | spine3 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 126 | spine4 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 127 | borderleaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: borderleaf2_Ethernet1 | PASS | - |
| 128 | borderleaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: borderleaf2_Ethernet2 | PASS | - |
| 129 | borderleaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1_Ethernet7 | PASS | - |
| 130 | borderleaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2_Ethernet7 | PASS | - |
| 131 | borderleaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3_Ethernet7 | PASS | - |
| 132 | borderleaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: spine4_Ethernet7 | PASS | - |
| 133 | borderleaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: borderleaf1_Ethernet1 | PASS | - |
| 134 | borderleaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: borderleaf1_Ethernet2 | PASS | - |
| 135 | borderleaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1_Ethernet8 | PASS | - |
| 136 | borderleaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2_Ethernet8 | PASS | - |
| 137 | borderleaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3_Ethernet8 | PASS | - |
| 138 | borderleaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: spine4_Ethernet8 | PASS | - |
| 139 | leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: leaf2_Ethernet1 | PASS | - |
| 140 | leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf2_Ethernet2 | PASS | - |
| 141 | leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1_Ethernet3 | PASS | - |
| 142 | leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2_Ethernet3 | PASS | - |
| 143 | leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3_Ethernet3 | PASS | - |
| 144 | leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: spine4_Ethernet3 | PASS | - |
| 145 | leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: leaf1_Ethernet1 | PASS | - |
| 146 | leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf1_Ethernet2 | PASS | - |
| 147 | leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1_Ethernet4 | PASS | - |
| 148 | leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2_Ethernet4 | PASS | - |
| 149 | leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3_Ethernet4 | PASS | - |
| 150 | leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: spine4_Ethernet4 | PASS | - |
| 151 | leaf3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1_Ethernet5 | PASS | - |
| 152 | leaf3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2_Ethernet5 | PASS | - |
| 153 | leaf3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3_Ethernet5 | PASS | - |
| 154 | leaf3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: spine4_Ethernet5 | PASS | - |
| 155 | leaf4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1_Ethernet6 | PASS | - |
| 156 | leaf4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2_Ethernet6 | PASS | - |
| 157 | leaf4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3_Ethernet6 | PASS | - |
| 158 | leaf4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: spine4_Ethernet6 | PASS | - |
| 159 | spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: leaf1_Ethernet3 | PASS | - |
| 160 | spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: leaf2_Ethernet3 | PASS | - |
| 161 | spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: leaf3_Ethernet3 | PASS | - |
| 162 | spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: leaf4_Ethernet3 | PASS | - |
| 163 | spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet7 - remote: borderleaf1_Ethernet3 | PASS | - |
| 164 | spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet8 - remote: borderleaf2_Ethernet3 | PASS | - |
| 165 | spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: leaf1_Ethernet4 | PASS | - |
| 166 | spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: leaf2_Ethernet4 | PASS | - |
| 167 | spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: leaf3_Ethernet4 | PASS | - |
| 168 | spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: leaf4_Ethernet4 | PASS | - |
| 169 | spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet7 - remote: borderleaf1_Ethernet4 | PASS | - |
| 170 | spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet8 - remote: borderleaf2_Ethernet4 | PASS | - |
| 171 | spine3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: leaf1_Ethernet5 | PASS | - |
| 172 | spine3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: leaf2_Ethernet5 | PASS | - |
| 173 | spine3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: leaf3_Ethernet5 | PASS | - |
| 174 | spine3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: leaf4_Ethernet5 | PASS | - |
| 175 | spine3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet7 - remote: borderleaf1_Ethernet5 | PASS | - |
| 176 | spine3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet8 - remote: borderleaf2_Ethernet5 | PASS | - |
| 177 | spine4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: leaf1_Ethernet6 | PASS | - |
| 178 | spine4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: leaf2_Ethernet6 | PASS | - |
| 179 | spine4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: leaf3_Ethernet6 | PASS | - |
| 180 | spine4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: leaf4_Ethernet6 | PASS | - |
| 181 | spine4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet7 - remote: borderleaf1_Ethernet6 | PASS | - |
| 182 | spine4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet8 - remote: borderleaf2_Ethernet6 | PASS | - |
| 183 | borderleaf1 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 184 | borderleaf2 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 185 | leaf1 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 186 | leaf2 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 187 | borderleaf1 | IP Reachability | ip reachability test p2p links | Source: borderleaf1_Ethernet3 - Destination: spine1_Ethernet7 | PASS | - |
| 188 | borderleaf1 | IP Reachability | ip reachability test p2p links | Source: borderleaf1_Ethernet4 - Destination: spine2_Ethernet7 | PASS | - |
| 189 | borderleaf1 | IP Reachability | ip reachability test p2p links | Source: borderleaf1_Ethernet5 - Destination: spine3_Ethernet7 | PASS | - |
| 190 | borderleaf1 | IP Reachability | ip reachability test p2p links | Source: borderleaf1_Ethernet6 - Destination: spine4_Ethernet7 | PASS | - |
| 191 | borderleaf2 | IP Reachability | ip reachability test p2p links | Source: borderleaf2_Ethernet3 - Destination: spine1_Ethernet8 | PASS | - |
| 192 | borderleaf2 | IP Reachability | ip reachability test p2p links | Source: borderleaf2_Ethernet4 - Destination: spine2_Ethernet8 | PASS | - |
| 193 | borderleaf2 | IP Reachability | ip reachability test p2p links | Source: borderleaf2_Ethernet5 - Destination: spine3_Ethernet8 | PASS | - |
| 194 | borderleaf2 | IP Reachability | ip reachability test p2p links | Source: borderleaf2_Ethernet6 - Destination: spine4_Ethernet8 | PASS | - |
| 195 | leaf1 | IP Reachability | ip reachability test p2p links | Source: leaf1_Ethernet3 - Destination: spine1_Ethernet3 | PASS | - |
| 196 | leaf1 | IP Reachability | ip reachability test p2p links | Source: leaf1_Ethernet4 - Destination: spine2_Ethernet3 | PASS | - |
| 197 | leaf1 | IP Reachability | ip reachability test p2p links | Source: leaf1_Ethernet5 - Destination: spine3_Ethernet3 | PASS | - |
| 198 | leaf1 | IP Reachability | ip reachability test p2p links | Source: leaf1_Ethernet6 - Destination: spine4_Ethernet3 | PASS | - |
| 199 | leaf2 | IP Reachability | ip reachability test p2p links | Source: leaf2_Ethernet3 - Destination: spine1_Ethernet4 | PASS | - |
| 200 | leaf2 | IP Reachability | ip reachability test p2p links | Source: leaf2_Ethernet4 - Destination: spine2_Ethernet4 | PASS | - |
| 201 | leaf2 | IP Reachability | ip reachability test p2p links | Source: leaf2_Ethernet5 - Destination: spine3_Ethernet4 | PASS | - |
| 202 | leaf2 | IP Reachability | ip reachability test p2p links | Source: leaf2_Ethernet6 - Destination: spine4_Ethernet4 | PASS | - |
| 203 | leaf3 | IP Reachability | ip reachability test p2p links | Source: leaf3_Ethernet3 - Destination: spine1_Ethernet5 | PASS | - |
| 204 | leaf3 | IP Reachability | ip reachability test p2p links | Source: leaf3_Ethernet4 - Destination: spine2_Ethernet5 | PASS | - |
| 205 | leaf3 | IP Reachability | ip reachability test p2p links | Source: leaf3_Ethernet5 - Destination: spine3_Ethernet5 | PASS | - |
| 206 | leaf3 | IP Reachability | ip reachability test p2p links | Source: leaf3_Ethernet6 - Destination: spine4_Ethernet5 | PASS | - |
| 207 | leaf4 | IP Reachability | ip reachability test p2p links | Source: leaf4_Ethernet3 - Destination: spine1_Ethernet6 | PASS | - |
| 208 | leaf4 | IP Reachability | ip reachability test p2p links | Source: leaf4_Ethernet4 - Destination: spine2_Ethernet6 | PASS | - |
| 209 | leaf4 | IP Reachability | ip reachability test p2p links | Source: leaf4_Ethernet5 - Destination: spine3_Ethernet6 | PASS | - |
| 210 | leaf4 | IP Reachability | ip reachability test p2p links | Source: leaf4_Ethernet6 - Destination: spine4_Ethernet6 | PASS | - |
| 211 | spine1 | IP Reachability | ip reachability test p2p links | Source: spine1_Ethernet3 - Destination: leaf1_Ethernet3 | PASS | - |
| 212 | spine1 | IP Reachability | ip reachability test p2p links | Source: spine1_Ethernet4 - Destination: leaf2_Ethernet3 | PASS | - |
| 213 | spine1 | IP Reachability | ip reachability test p2p links | Source: spine1_Ethernet5 - Destination: leaf3_Ethernet3 | PASS | - |
| 214 | spine1 | IP Reachability | ip reachability test p2p links | Source: spine1_Ethernet6 - Destination: leaf4_Ethernet3 | PASS | - |
| 215 | spine1 | IP Reachability | ip reachability test p2p links | Source: spine1_Ethernet7 - Destination: borderleaf1_Ethernet3 | PASS | - |
| 216 | spine1 | IP Reachability | ip reachability test p2p links | Source: spine1_Ethernet8 - Destination: borderleaf2_Ethernet3 | PASS | - |
| 217 | spine2 | IP Reachability | ip reachability test p2p links | Source: spine2_Ethernet3 - Destination: leaf1_Ethernet4 | PASS | - |
| 218 | spine2 | IP Reachability | ip reachability test p2p links | Source: spine2_Ethernet4 - Destination: leaf2_Ethernet4 | PASS | - |
| 219 | spine2 | IP Reachability | ip reachability test p2p links | Source: spine2_Ethernet5 - Destination: leaf3_Ethernet4 | PASS | - |
| 220 | spine2 | IP Reachability | ip reachability test p2p links | Source: spine2_Ethernet6 - Destination: leaf4_Ethernet4 | PASS | - |
| 221 | spine2 | IP Reachability | ip reachability test p2p links | Source: spine2_Ethernet7 - Destination: borderleaf1_Ethernet4 | PASS | - |
| 222 | spine2 | IP Reachability | ip reachability test p2p links | Source: spine2_Ethernet8 - Destination: borderleaf2_Ethernet4 | PASS | - |
| 223 | spine3 | IP Reachability | ip reachability test p2p links | Source: spine3_Ethernet3 - Destination: leaf1_Ethernet5 | PASS | - |
| 224 | spine3 | IP Reachability | ip reachability test p2p links | Source: spine3_Ethernet4 - Destination: leaf2_Ethernet5 | PASS | - |
| 225 | spine3 | IP Reachability | ip reachability test p2p links | Source: spine3_Ethernet5 - Destination: leaf3_Ethernet5 | PASS | - |
| 226 | spine3 | IP Reachability | ip reachability test p2p links | Source: spine3_Ethernet6 - Destination: leaf4_Ethernet5 | PASS | - |
| 227 | spine3 | IP Reachability | ip reachability test p2p links | Source: spine3_Ethernet7 - Destination: borderleaf1_Ethernet5 | PASS | - |
| 228 | spine3 | IP Reachability | ip reachability test p2p links | Source: spine3_Ethernet8 - Destination: borderleaf2_Ethernet5 | PASS | - |
| 229 | spine4 | IP Reachability | ip reachability test p2p links | Source: spine4_Ethernet3 - Destination: leaf1_Ethernet6 | PASS | - |
| 230 | spine4 | IP Reachability | ip reachability test p2p links | Source: spine4_Ethernet4 - Destination: leaf2_Ethernet6 | PASS | - |
| 231 | spine4 | IP Reachability | ip reachability test p2p links | Source: spine4_Ethernet5 - Destination: leaf3_Ethernet6 | PASS | - |
| 232 | spine4 | IP Reachability | ip reachability test p2p links | Source: spine4_Ethernet6 - Destination: leaf4_Ethernet6 | PASS | - |
| 233 | spine4 | IP Reachability | ip reachability test p2p links | Source: spine4_Ethernet7 - Destination: borderleaf1_Ethernet6 | PASS | - |
| 234 | spine4 | IP Reachability | ip reachability test p2p links | Source: spine4_Ethernet8 - Destination: borderleaf2_Ethernet6 | PASS | - |
| 235 | borderleaf1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 236 | borderleaf2 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 237 | leaf1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 238 | leaf2 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 239 | leaf3 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 240 | leaf4 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 241 | spine1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 242 | spine2 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 243 | spine3 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 244 | spine4 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 245 | borderleaf1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.253.9 | PASS | - |
| 246 | borderleaf1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.32 | PASS | - |
| 247 | borderleaf1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.34 | PASS | - |
| 248 | borderleaf1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.36 | PASS | - |
| 249 | borderleaf1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.38 | PASS | - |
| 250 | borderleaf2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.253.8 | PASS | - |
| 251 | borderleaf2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.40 | PASS | - |
| 252 | borderleaf2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.42 | PASS | - |
| 253 | borderleaf2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.44 | PASS | - |
| 254 | borderleaf2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.46 | PASS | - |
| 255 | leaf1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.253.1 | PASS | - |
| 256 | leaf1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.0 | PASS | - |
| 257 | leaf1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.2 | PASS | - |
| 258 | leaf1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.4 | PASS | - |
| 259 | leaf1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.6 | PASS | - |
| 260 | leaf2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.253.0 | PASS | - |
| 261 | leaf2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.8 | PASS | - |
| 262 | leaf2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.10 | PASS | - |
| 263 | leaf2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.12 | PASS | - |
| 264 | leaf2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.14 | PASS | - |
| 265 | leaf3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.16 | PASS | - |
| 266 | leaf3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.18 | PASS | - |
| 267 | leaf3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.20 | PASS | - |
| 268 | leaf3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.22 | PASS | - |
| 269 | leaf4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.24 | PASS | - |
| 270 | leaf4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.26 | PASS | - |
| 271 | leaf4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.28 | PASS | - |
| 272 | leaf4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.30 | PASS | - |
| 273 | spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.1 | PASS | - |
| 274 | spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.9 | PASS | - |
| 275 | spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.17 | PASS | - |
| 276 | spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.25 | PASS | - |
| 277 | spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.33 | PASS | - |
| 278 | spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.41 | PASS | - |
| 279 | spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.3 | PASS | - |
| 280 | spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.11 | PASS | - |
| 281 | spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.19 | PASS | - |
| 282 | spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.27 | PASS | - |
| 283 | spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.35 | PASS | - |
| 284 | spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.43 | PASS | - |
| 285 | spine3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.5 | PASS | - |
| 286 | spine3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.13 | PASS | - |
| 287 | spine3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.21 | PASS | - |
| 288 | spine3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.29 | PASS | - |
| 289 | spine3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.37 | PASS | - |
| 290 | spine3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.45 | PASS | - |
| 291 | spine4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.7 | PASS | - |
| 292 | spine4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.15 | PASS | - |
| 293 | spine4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.23 | PASS | - |
| 294 | spine4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.31 | PASS | - |
| 295 | spine4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.39 | PASS | - |
| 296 | spine4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.1.47 | PASS | - |
| 297 | borderleaf1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.107 | PASS | - |
| 298 | borderleaf1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.108 | PASS | - |
| 299 | borderleaf1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.109 | PASS | - |
| 300 | borderleaf1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.110 | PASS | - |
| 301 | borderleaf2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.107 | PASS | - |
| 302 | borderleaf2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.108 | PASS | - |
| 303 | borderleaf2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.109 | PASS | - |
| 304 | borderleaf2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.110 | PASS | - |
| 305 | leaf1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.107 | PASS | - |
| 306 | leaf1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.108 | PASS | - |
| 307 | leaf1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.109 | PASS | - |
| 308 | leaf1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.110 | PASS | - |
| 309 | leaf2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.107 | PASS | - |
| 310 | leaf2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.108 | PASS | - |
| 311 | leaf2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.109 | PASS | - |
| 312 | leaf2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.110 | PASS | - |
| 313 | leaf3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.107 | PASS | - |
| 314 | leaf3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.108 | PASS | - |
| 315 | leaf3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.109 | PASS | - |
| 316 | leaf3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.110 | PASS | - |
| 317 | leaf4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.107 | PASS | - |
| 318 | leaf4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.108 | PASS | - |
| 319 | leaf4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.109 | PASS | - |
| 320 | leaf4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.110 | PASS | - |
| 321 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.69 | PASS | - |
| 322 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.70 | PASS | - |
| 323 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.65 | PASS | - |
| 324 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.66 | PASS | - |
| 325 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.67 | PASS | - |
| 326 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.68 | PASS | - |
| 327 | spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.69 | PASS | - |
| 328 | spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.70 | PASS | - |
| 329 | spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.65 | PASS | - |
| 330 | spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.66 | PASS | - |
| 331 | spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.67 | PASS | - |
| 332 | spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.68 | PASS | - |
| 333 | spine3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.69 | PASS | - |
| 334 | spine3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.70 | PASS | - |
| 335 | spine3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.65 | PASS | - |
| 336 | spine3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.66 | PASS | - |
| 337 | spine3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.67 | PASS | - |
| 338 | spine3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.68 | PASS | - |
| 339 | spine4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.69 | PASS | - |
| 340 | spine4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.70 | PASS | - |
| 341 | spine4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.65 | PASS | - |
| 342 | spine4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.66 | PASS | - |
| 343 | spine4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.67 | PASS | - |
| 344 | spine4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 172.16.0.68 | PASS | - |
| 345 | borderleaf1 | Routing Table | Remote VTEP address | 172.16.1.69 | PASS | - |
| 346 | borderleaf1 | Routing Table | Remote VTEP address | 172.16.1.65 | PASS | - |
| 347 | borderleaf1 | Routing Table | Remote VTEP address | 172.16.1.67 | PASS | - |
| 348 | borderleaf1 | Routing Table | Remote VTEP address | 172.16.1.68 | PASS | - |
| 349 | borderleaf2 | Routing Table | Remote VTEP address | 172.16.1.69 | PASS | - |
| 350 | borderleaf2 | Routing Table | Remote VTEP address | 172.16.1.65 | PASS | - |
| 351 | borderleaf2 | Routing Table | Remote VTEP address | 172.16.1.67 | PASS | - |
| 352 | borderleaf2 | Routing Table | Remote VTEP address | 172.16.1.68 | PASS | - |
| 353 | leaf1 | Routing Table | Remote VTEP address | 172.16.1.69 | PASS | - |
| 354 | leaf1 | Routing Table | Remote VTEP address | 172.16.1.65 | PASS | - |
| 355 | leaf1 | Routing Table | Remote VTEP address | 172.16.1.67 | PASS | - |
| 356 | leaf1 | Routing Table | Remote VTEP address | 172.16.1.68 | PASS | - |
| 357 | leaf2 | Routing Table | Remote VTEP address | 172.16.1.69 | PASS | - |
| 358 | leaf2 | Routing Table | Remote VTEP address | 172.16.1.65 | PASS | - |
| 359 | leaf2 | Routing Table | Remote VTEP address | 172.16.1.67 | PASS | - |
| 360 | leaf2 | Routing Table | Remote VTEP address | 172.16.1.68 | PASS | - |
| 361 | leaf3 | Routing Table | Remote VTEP address | 172.16.1.69 | PASS | - |
| 362 | leaf3 | Routing Table | Remote VTEP address | 172.16.1.65 | PASS | - |
| 363 | leaf3 | Routing Table | Remote VTEP address | 172.16.1.67 | PASS | - |
| 364 | leaf3 | Routing Table | Remote VTEP address | 172.16.1.68 | PASS | - |
| 365 | leaf4 | Routing Table | Remote VTEP address | 172.16.1.69 | PASS | - |
| 366 | leaf4 | Routing Table | Remote VTEP address | 172.16.1.65 | PASS | - |
| 367 | leaf4 | Routing Table | Remote VTEP address | 172.16.1.67 | PASS | - |
| 368 | leaf4 | Routing Table | Remote VTEP address | 172.16.1.68 | PASS | - |
| 369 | borderleaf1 | Routing Table | Remote Lo0 address | 172.16.0.69 | PASS | - |
| 370 | borderleaf1 | Routing Table | Remote Lo0 address | 172.16.0.70 | PASS | - |
| 371 | borderleaf1 | Routing Table | Remote Lo0 address | 172.16.0.65 | PASS | - |
| 372 | borderleaf1 | Routing Table | Remote Lo0 address | 172.16.0.66 | PASS | - |
| 373 | borderleaf1 | Routing Table | Remote Lo0 address | 172.16.0.67 | PASS | - |
| 374 | borderleaf1 | Routing Table | Remote Lo0 address | 172.16.0.68 | PASS | - |
| 375 | borderleaf1 | Routing Table | Remote Lo0 address | 172.16.0.107 | PASS | - |
| 376 | borderleaf1 | Routing Table | Remote Lo0 address | 172.16.0.108 | PASS | - |
| 377 | borderleaf1 | Routing Table | Remote Lo0 address | 172.16.0.109 | PASS | - |
| 378 | borderleaf1 | Routing Table | Remote Lo0 address | 172.16.0.110 | PASS | - |
| 379 | borderleaf2 | Routing Table | Remote Lo0 address | 172.16.0.69 | PASS | - |
| 380 | borderleaf2 | Routing Table | Remote Lo0 address | 172.16.0.70 | PASS | - |
| 381 | borderleaf2 | Routing Table | Remote Lo0 address | 172.16.0.65 | PASS | - |
| 382 | borderleaf2 | Routing Table | Remote Lo0 address | 172.16.0.66 | PASS | - |
| 383 | borderleaf2 | Routing Table | Remote Lo0 address | 172.16.0.67 | PASS | - |
| 384 | borderleaf2 | Routing Table | Remote Lo0 address | 172.16.0.68 | PASS | - |
| 385 | borderleaf2 | Routing Table | Remote Lo0 address | 172.16.0.107 | PASS | - |
| 386 | borderleaf2 | Routing Table | Remote Lo0 address | 172.16.0.108 | PASS | - |
| 387 | borderleaf2 | Routing Table | Remote Lo0 address | 172.16.0.109 | PASS | - |
| 388 | borderleaf2 | Routing Table | Remote Lo0 address | 172.16.0.110 | PASS | - |
| 389 | leaf1 | Routing Table | Remote Lo0 address | 172.16.0.69 | PASS | - |
| 390 | leaf1 | Routing Table | Remote Lo0 address | 172.16.0.70 | PASS | - |
| 391 | leaf1 | Routing Table | Remote Lo0 address | 172.16.0.65 | PASS | - |
| 392 | leaf1 | Routing Table | Remote Lo0 address | 172.16.0.66 | PASS | - |
| 393 | leaf1 | Routing Table | Remote Lo0 address | 172.16.0.67 | PASS | - |
| 394 | leaf1 | Routing Table | Remote Lo0 address | 172.16.0.68 | PASS | - |
| 395 | leaf1 | Routing Table | Remote Lo0 address | 172.16.0.107 | PASS | - |
| 396 | leaf1 | Routing Table | Remote Lo0 address | 172.16.0.108 | PASS | - |
| 397 | leaf1 | Routing Table | Remote Lo0 address | 172.16.0.109 | PASS | - |
| 398 | leaf1 | Routing Table | Remote Lo0 address | 172.16.0.110 | PASS | - |
| 399 | leaf2 | Routing Table | Remote Lo0 address | 172.16.0.69 | PASS | - |
| 400 | leaf2 | Routing Table | Remote Lo0 address | 172.16.0.70 | PASS | - |
| 401 | leaf2 | Routing Table | Remote Lo0 address | 172.16.0.65 | PASS | - |
| 402 | leaf2 | Routing Table | Remote Lo0 address | 172.16.0.66 | PASS | - |
| 403 | leaf2 | Routing Table | Remote Lo0 address | 172.16.0.67 | PASS | - |
| 404 | leaf2 | Routing Table | Remote Lo0 address | 172.16.0.68 | PASS | - |
| 405 | leaf2 | Routing Table | Remote Lo0 address | 172.16.0.107 | PASS | - |
| 406 | leaf2 | Routing Table | Remote Lo0 address | 172.16.0.108 | PASS | - |
| 407 | leaf2 | Routing Table | Remote Lo0 address | 172.16.0.109 | PASS | - |
| 408 | leaf2 | Routing Table | Remote Lo0 address | 172.16.0.110 | PASS | - |
| 409 | leaf3 | Routing Table | Remote Lo0 address | 172.16.0.69 | PASS | - |
| 410 | leaf3 | Routing Table | Remote Lo0 address | 172.16.0.70 | PASS | - |
| 411 | leaf3 | Routing Table | Remote Lo0 address | 172.16.0.65 | PASS | - |
| 412 | leaf3 | Routing Table | Remote Lo0 address | 172.16.0.66 | PASS | - |
| 413 | leaf3 | Routing Table | Remote Lo0 address | 172.16.0.67 | PASS | - |
| 414 | leaf3 | Routing Table | Remote Lo0 address | 172.16.0.68 | PASS | - |
| 415 | leaf3 | Routing Table | Remote Lo0 address | 172.16.0.107 | PASS | - |
| 416 | leaf3 | Routing Table | Remote Lo0 address | 172.16.0.108 | PASS | - |
| 417 | leaf3 | Routing Table | Remote Lo0 address | 172.16.0.109 | PASS | - |
| 418 | leaf3 | Routing Table | Remote Lo0 address | 172.16.0.110 | PASS | - |
| 419 | leaf4 | Routing Table | Remote Lo0 address | 172.16.0.69 | PASS | - |
| 420 | leaf4 | Routing Table | Remote Lo0 address | 172.16.0.70 | PASS | - |
| 421 | leaf4 | Routing Table | Remote Lo0 address | 172.16.0.65 | PASS | - |
| 422 | leaf4 | Routing Table | Remote Lo0 address | 172.16.0.66 | PASS | - |
| 423 | leaf4 | Routing Table | Remote Lo0 address | 172.16.0.67 | PASS | - |
| 424 | leaf4 | Routing Table | Remote Lo0 address | 172.16.0.68 | PASS | - |
| 425 | leaf4 | Routing Table | Remote Lo0 address | 172.16.0.107 | PASS | - |
| 426 | leaf4 | Routing Table | Remote Lo0 address | 172.16.0.108 | PASS | - |
| 427 | leaf4 | Routing Table | Remote Lo0 address | 172.16.0.109 | PASS | - |
| 428 | leaf4 | Routing Table | Remote Lo0 address | 172.16.0.110 | PASS | - |
| 429 | borderleaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1 - 172.16.0.69 Destination: 172.16.0.69 | PASS | - |
| 430 | borderleaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1 - 172.16.0.69 Destination: 172.16.0.70 | PASS | - |
| 431 | borderleaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1 - 172.16.0.69 Destination: 172.16.0.65 | PASS | - |
| 432 | borderleaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1 - 172.16.0.69 Destination: 172.16.0.66 | PASS | - |
| 433 | borderleaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1 - 172.16.0.69 Destination: 172.16.0.67 | PASS | - |
| 434 | borderleaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1 - 172.16.0.69 Destination: 172.16.0.68 | PASS | - |
| 435 | borderleaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1 - 172.16.0.69 Destination: 172.16.0.107 | PASS | - |
| 436 | borderleaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1 - 172.16.0.69 Destination: 172.16.0.108 | PASS | - |
| 437 | borderleaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1 - 172.16.0.69 Destination: 172.16.0.109 | PASS | - |
| 438 | borderleaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1 - 172.16.0.69 Destination: 172.16.0.110 | PASS | - |
| 439 | borderleaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2 - 172.16.0.70 Destination: 172.16.0.69 | PASS | - |
| 440 | borderleaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2 - 172.16.0.70 Destination: 172.16.0.70 | PASS | - |
| 441 | borderleaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2 - 172.16.0.70 Destination: 172.16.0.65 | PASS | - |
| 442 | borderleaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2 - 172.16.0.70 Destination: 172.16.0.66 | PASS | - |
| 443 | borderleaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2 - 172.16.0.70 Destination: 172.16.0.67 | PASS | - |
| 444 | borderleaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2 - 172.16.0.70 Destination: 172.16.0.68 | PASS | - |
| 445 | borderleaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2 - 172.16.0.70 Destination: 172.16.0.107 | PASS | - |
| 446 | borderleaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2 - 172.16.0.70 Destination: 172.16.0.108 | PASS | - |
| 447 | borderleaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2 - 172.16.0.70 Destination: 172.16.0.109 | PASS | - |
| 448 | borderleaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2 - 172.16.0.70 Destination: 172.16.0.110 | PASS | - |
| 449 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 172.16.0.65 Destination: 172.16.0.69 | PASS | - |
| 450 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 172.16.0.65 Destination: 172.16.0.70 | PASS | - |
| 451 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 172.16.0.65 Destination: 172.16.0.65 | PASS | - |
| 452 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 172.16.0.65 Destination: 172.16.0.66 | PASS | - |
| 453 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 172.16.0.65 Destination: 172.16.0.67 | PASS | - |
| 454 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 172.16.0.65 Destination: 172.16.0.68 | PASS | - |
| 455 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 172.16.0.65 Destination: 172.16.0.107 | PASS | - |
| 456 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 172.16.0.65 Destination: 172.16.0.108 | PASS | - |
| 457 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 172.16.0.65 Destination: 172.16.0.109 | PASS | - |
| 458 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 172.16.0.65 Destination: 172.16.0.110 | PASS | - |
| 459 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 172.16.0.66 Destination: 172.16.0.69 | PASS | - |
| 460 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 172.16.0.66 Destination: 172.16.0.70 | PASS | - |
| 461 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 172.16.0.66 Destination: 172.16.0.65 | PASS | - |
| 462 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 172.16.0.66 Destination: 172.16.0.66 | PASS | - |
| 463 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 172.16.0.66 Destination: 172.16.0.67 | PASS | - |
| 464 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 172.16.0.66 Destination: 172.16.0.68 | PASS | - |
| 465 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 172.16.0.66 Destination: 172.16.0.107 | PASS | - |
| 466 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 172.16.0.66 Destination: 172.16.0.108 | PASS | - |
| 467 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 172.16.0.66 Destination: 172.16.0.109 | PASS | - |
| 468 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 172.16.0.66 Destination: 172.16.0.110 | PASS | - |
| 469 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 172.16.0.67 Destination: 172.16.0.69 | PASS | - |
| 470 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 172.16.0.67 Destination: 172.16.0.70 | PASS | - |
| 471 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 172.16.0.67 Destination: 172.16.0.65 | PASS | - |
| 472 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 172.16.0.67 Destination: 172.16.0.66 | PASS | - |
| 473 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 172.16.0.67 Destination: 172.16.0.67 | PASS | - |
| 474 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 172.16.0.67 Destination: 172.16.0.68 | PASS | - |
| 475 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 172.16.0.67 Destination: 172.16.0.107 | PASS | - |
| 476 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 172.16.0.67 Destination: 172.16.0.108 | PASS | - |
| 477 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 172.16.0.67 Destination: 172.16.0.109 | PASS | - |
| 478 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 172.16.0.67 Destination: 172.16.0.110 | PASS | - |
| 479 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 172.16.0.68 Destination: 172.16.0.69 | PASS | - |
| 480 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 172.16.0.68 Destination: 172.16.0.70 | PASS | - |
| 481 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 172.16.0.68 Destination: 172.16.0.65 | PASS | - |
| 482 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 172.16.0.68 Destination: 172.16.0.66 | PASS | - |
| 483 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 172.16.0.68 Destination: 172.16.0.67 | PASS | - |
| 484 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 172.16.0.68 Destination: 172.16.0.68 | PASS | - |
| 485 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 172.16.0.68 Destination: 172.16.0.107 | PASS | - |
| 486 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 172.16.0.68 Destination: 172.16.0.108 | PASS | - |
| 487 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 172.16.0.68 Destination: 172.16.0.109 | PASS | - |
| 488 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 172.16.0.68 Destination: 172.16.0.110 | PASS | - |
