# Test Case #9: Network Automation 

#### Automate the backup of network device configurations for the core and distribution layer on a weekly basis. Retrieve device configurations, and store them in a centralized location for easy access and disaster recovery.


## Functionality
A python script from the ansible device will log into 2 vyos routers and an exos switch and save their configurations. The script will run ‘show configuration’, and write the contents to a file that will be stored on the storage server. 

A cron job will make sure this task runs every Saturday night at 10pm.

## Network Diagram Segment

## Testing Method
On the storage server, check the folder to make sure backups are there. File names will indicate the device of the backup.
`ls /home/student/backups`

## Process List
Use the configbackup.py script  

#Python libraries will be required  
`sudo apt install python3`  
`sudo apt install python3-pip`  
`pip install paramiko`  
`pip install netmiko`  


Run the script  
`cd /home/student/python`  
`python3 configbackup.py`  



To configure this script to run every Saturday at 10pm, open crontab on the ansible desktop:  
`crontab –e`  

Add this line at the end:  
`0 22 * * 6 /usr/bin/python3 home/student/python/configpython.py`
