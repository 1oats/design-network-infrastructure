# Test Case #1: Device Discovery and Reachability 
#### Your network solution must include multiple network segments with access controls that allow traffic from a device on one network to access the resources of a device on another network. Similarly, there must be devices on one network that cannot access resources on a different network.

## Functionality
Guest devices on the guest network should not be able to access the Syslog server and NTP server in the demilitarized zone.  

User devices in the user network should not be able to access the management network, and monitoring network that is connected to the main switch. I created ACL policies for the main switch through the web interface.  

Guest devices should not be able to access the internal network on 10.10.1.1  

## Network Diagram Segment

## Testing Method
Ping the destination address of the access control list to see if there is a response. From the Guest device:  
From 10.10.12.10, `ping 10.10.11.11`  
From 10.10.12.10 ping `10.10.11.12`  
From 10.10.12.10, ping any 10.10.x.x address in the internal network  

There should be no response due to the ACL on the edge router and firewall.  

From the user network, ping the Monitoring and Management server. From User1 on the User Network  
From 10.10.15.11, `ping 10.10.14.10`  
From 10.10.15.11 `ping 10.10.16.10`  
<br>
There should be no response due to the ACL on the distribution switch.  


## Process List

On the edge router, configure the ACL rule and attach it to an interface.

`set firewall name dmz rule 20 source address 10.10.12.0/24`  
`set firewall name dmz rule 20 destination address 10.10.11.0/24`  
`set firewall name dmz rule 20 action reject`  

`Set interfaces ethernet eth2 firewall out name dmz`  


Deny the guest subnet (10.10.12.0/24) to all internal subnets on 10.10.0.0/16  

`set firewall name denyall rule 100 source address 10.10.12.0/24`  
`set firewall name denyall rule 100 destination address 10.10.0.0/16`  
`set firewall name denyall rule 100 action reject`  
`Set interfaces ethernet eth1 firewall out name denyall`  
`Commit`  
`save`  




On firewall, block the guest network from being able to reach the internet network  
`set firewall name guest rule 20 source address 10.10.12.0/24`  
`Set firewall name guest rule 20 destination address 10.10.1.0/24`  
`Set firewall name guest rule 20 action reject`  
`Set interfaces ethernet eth1 firewall out name guest`  
`Commit`  
`save`  




On the distribution switch, I used the web interface to deny access to the Management (10.10.13.1/24) and Monitoring network (10.10.17.1/24) from the User device network (10.10.15.1/24)
<br>  
First, enable the web interface on the switch  
 `Enable web http`  
 <br>
 
Then log in to the web interface from a device on the user network (User1), by entering 10.10.15.1 in the firefox web browser.






