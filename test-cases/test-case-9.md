# Test Case #9: Network Automation 

#### Automate the backup of network device configurations for the core and distribution layer on a weekly basis. Retrieve device configurations, and store them in a centralized location for easy access and disaster recovery.

## Functionality
A python script from the ansible device will log into 2 vyos routers and an exos switch and save their configurations. The script will run ‘show configuration’, and write the contents to a file that will be stored on the storage server. 

A cron job will make sure this task runs every Saturday night at 10pm.
<br>
## Network Diagram Segment
<br>
<div align="center">
  <img src="../screenshots/t9/diagram9.png" alt="diagram 9" width="700">
</div>
<div align="center">
  <img src="../screenshots/t9/core_legend.png" alt="core legend" width="345">
  <img src="../screenshots/t9/server_legend.png" alt="server legend" width="345">
</div>
<br><br>

## Testing Method
On the storage server, check the folder to make sure backups are there. File names will indicate the device of the backup.
`ls /home/student/backups`
<br><br>

## Process List
Use the configbackup.py script  

Python libraries will be required  
`sudo apt install python3`  
`sudo apt install python3-pip`  
`pip install paramiko`  
`pip install netmiko`  


Run the script  
`cd /home/student/python`  
`python3 configbackup.py`  
<br><br>
<div align="center">
  <p>Files are stored locally in home/student/backups before being sent to the storage server successfully</p>
  <img src="../screenshots/t9/local_backups.png" alt="local backups" width="700">
</div>
<br><br>
<div align="center">
  <p>Verification that files are properly stored on the storage server</p>
  <img src="../screenshots/t9/storage_backups.png" alt="storage backups" width="700">
</div>
<br><br>

To configure this script to run every Saturday at 10pm, open crontab on the ansible desktop:  
`crontab –e`  

Add this line at the end:  
`0 22 * * 6 /usr/bin/python3 home/student/python/configpython.py`  
<br><br>
<div align="center">
  <img src="../screenshots/t9/crontab.png" alt="crontab -e" width="700">
</div>
<br><br>

##  Edgerouter configuration backup
<div align="center">
  <img src="../screenshots/t9/edge_config_1.png" alt="edge config 1" width="700">
  <img src="../screenshots/t9/edge_config_2.png" alt="edge config 2" width="700">
  <img src="../screenshots/t9/edge_config_3.png" alt="edge config 3" width="700">
  <img src="../screenshots/t9/edge_config_4.png" alt="edge config 4" width="700">
  <img src="../screenshots/t9/edge_config_5.png" alt="edge config 5" width="700">
  <img src="../screenshots/t9/edge_config_6.png" alt="edge config 6" width="700">
</div>
<br><br>

## Firewall configuration backup
<div align="center">
  <img src="../screenshots/t9/firewall1.png" alt="firewall config 1" width="700">
  <img src="../screenshots/t9/firewall2.png" alt="firewall config 2" width="700">
  <img src="../screenshots/t9/firewall3.png" alt="firewall config 3" width="700">
</div>
<br><br>

## Distribution Switch configuration backup</p>
<div align="center">
  <img src="../screenshots/t9/switch1.png" alt="switch config 1" width="700">
  <img src="../screenshots/t9/switch2.png" alt="switch config 2" width="700">
  <img src="../screenshots/t9/switch3.png" alt="switch config 3" width="700">
</div>
<br><br>
