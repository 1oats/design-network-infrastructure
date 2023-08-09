# Test Case #2: Administering an Access Control List for Guest Access 

#### Your network must utilize an Access Control List that allows guest access. Guest access should be limited to internet traffic only.


## Functionality
Guest devices in the guest network will be able to access internet traffic only. It should not have access to the internal network.


## Network Diagram Segment
<br>
<div align="center">
  <img src="../screenshots/t2/diagram2.png" alt="ip" width="700">
</div>
<div align="center">
  <img src="../screenshots/t2/core_legend.png" alt="core" width="345">
  <img src="../screenshots/t2/device_legend.png" alt="server" legend" width="345">
 
</div>

## Testing Method
From the Guest device, ping internal networks to make sure they are not reachable. The guest device should be able to reach the external internet at 8.8.8.8  


## Process List
Create a firewall rule to allow connections from the Guest_Network to the Public Internet, on the Edge Router.  

`set firewall name guest rule 30 source address 10.10.12.0/24`  
`set firewall name guest rule 30 destination address 192.168.0.0/24`  
`set firewall name guest rule 30 action accept`  
`Set interfaces ethernet eth3 firewall out name guest`  
`commit`  
`save`  

<div align="center">
 <p>`show firewall name guest` and 'show interface ethernet eth3' for the guest access list</p>
  <img src="../screenshots/t2/show_firewall_interface.png" alt="firewall interface" width="600">
</div>
<br><br><br>
<div align="center">
 <p>Guest device can ping the public network, at 8.8.8.8, but cannot ping internal devices
</p>
  <img src="../screenshots/t2/acl_ping.png" alt="acl ping" width="600">
</div>
