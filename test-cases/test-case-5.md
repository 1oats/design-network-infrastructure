# Test Case #5: Layer 2 Link Redundancy and Spanning-Tree Protocol (802.1w)  
#### Enable and manage the Spanning-Tree Protocol to establish redundant Layer 2 paths while avoiding possible loops and broadcast storms. Identify the Layer 2 devices that will become the Root Bridge. 


## Functionality
The internet comes in through the vyos edge router, then vyos router2, then distribution switch (exos) before splitting off to the internal networks, and the distribution switch has several vlans attached on several interfaces. 
This particular network has no redundant paths for incoming and outgoing traffic, so the distribution switch which splits traffic within the internal network will be configured as the root bridge. It should have the lowest priority at 4096.
 


## Network Diagram Segment

## Testing Method
On the distribution switch, verify that stpd is configured.  
 `show stpd s0`  


### Process List
 Exos router comes default with MSTP. The default stp name is ‘s0’ and it is bound to the ‘Default’ Vlan. With auto-bind as the default configuration, all VLANS on the switch are attached to ‘s0’.  

Run this command to configure STP on the distribution switch:  
`configure stp s0 priority 4096`  

Check that STP has been configured.  
`show stpd s0`

