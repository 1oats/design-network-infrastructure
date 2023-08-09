# Test Case #3: Security Compliance—Log-in Banners and Automation 

#### Display a log-in banner when accessing each device on the network. The log-in banner should notify users of an acceptable use policy (AUP) or other security-based policies when attempting to log into the network. 

#### Additionally, establish an automated process to update the log-in banner for multiple devices. Clearly identify the devices that will be updated, and provide a step-by-step guide for initiating the automated updates. 
#### Note: Remove the banners prior to submission

## Functionality
 We will need to have the proper modules installed for ansible. Target devices will be defined in an inventory, and SSH must be enabled.  

The playbook will read the contents of the banner file, located in files/banner.txt and set the content as the post-login banner. The banner file can be edited and pushed via the playbook easily, so users are updated with new welcome notifications continuously.


## Network Diagram Segment

## Testing Method
Make sure that SSH is enabled on Ubuntu desktops:  

`Sudo systemctl status ssh`  

Before running a playbook, make sure that the ansible desktop can communicate via SSH with target devices. This will help determine if there are pre-existing connectivity issues that are SSH related, or ansible related.  

Then, test if a proper ansible connection exists with the proper inventory credentials and network connectivity tags. Ansible ping will work for linux, vyos, and exos devices, whereas win_ping will work with windows devices.  

`ansible windows -m win_ping -i inv.ini`  
`Ansible all –m ping –i inv.ini –e “ansible_become_password=P@ssw0rd”`  

Since the commands for all 4 types of devices were different, it is important to use the proper commands within the right module to properly execute the task. Google research were helpful in finding specifications, folder locations, and registry key locations, but documentation from ansible modules as well as examples were the most helpful in finding the right direction. Using commands such as exos_config and vyos_config were problematic, so verbose outputs were used to troubleshoot error messages in failed playbooks.  

When testing different commands, use –vvv for verbose error outputs:

    `Ansible-playbook –i inv.ini banners.yml –e “ansible_become_password=P@ssw0rd” -vvv`  

Other flags were also used at times, such as –vvvv for more error messages, and —limit <IP> to isolate one device for testing. A sample may look look:  

    `Ansible-playbook –i inv.ini banners.yml –e “ansible_become_password=P@ssw0rd” —limit 10.10.2.2 -vvvv`   

If the playbook runs successfully check that the post-login banner is changed by logging in to each device and visually confirm it. The banner will display when you enter or after you enter your credentials.  

Once logged into the Operating System of the device, you can see the post-login banner any time.  

In the edge router or firewall (vyos):    
`config`  
`Show system login banner`  

In the distribution switch (Exos):  
`Show banner`  

In Linux devices:  
`Cat /etc/motd`  

In Windows desktops:  
Enter Ctrl+R and `secpol` to open the Local Security Policy  
Under Local Policies > Security Options  
Look for `Interactive login: Message text...` and `Interactive: Message title...` to make sure the banner contents are set.  
 


### Process List
Use the banner.yml, inv.ini, exos_banner.sh, and files/banner.txt in the GitLab repository


We need to install and enable SSH on the target Ubuntu linux desktops  
  `sudo apt update`  
  `sudo apt install openssh-server`  


For the windows desktops, we need to add WinRM and open the firewall  
`winrm quickconfig`  
`winrm enumerate winrm/config/Listener`  
`configure firewall 5985`  

For the ansible desktop, we need to install the proper modules for ansible  
`sudo apt install python3`  
`sudo apt install python3-pip`  
`pip install paramiko`  
`sudo apt install ansible`  
`sudo apt-get install build-essential libssl-dev libffi-dev -y`  
`sudo ansible-galaxy collection install ansible.netcommon`  
`sudo ansible-galaxy collection install extreme.exos`  
`sudo ansible-galaxy collection install community.network`  

Install piwinrm to work with winrm  
`Pip install pywinrm`  

Install necessary ssh components for the ansible desktop:  
`Ssh-keygen`  
`ssh-agent bash`  
`ssh-add ~/.ssh/id_rsa`  
`Sudo apt-get install sshpass`  


Ansible will not check for host key verification  
`Sudo nano /etc/ansible/ansible.cfg`
````
[defaults]
Host_key_checking = False
````  

Run visudo command as root  
`sudo visudo`  
And add  
    `ansible_user ALL=(ALL) NOPASSWD:ALL`  

Prepare the switch by enabling ssh and creating a new admin user for ansible.   
`Enable ssh2`  
`Create account admin XXXXXX XXXXXX`  

You will need to either add the exos switch as an authorized host, or ssh into it so the device is recognized, before running an ansible playbook.




Run the playbook in /home/student/ansible:  
`Ansible-playbook –i inv.ini banners.yml –e “ansible_become_password=P@ssw0rd”`  

<br>

If banners needed to be removed before running the playbook, use the following commands:  

In Vyos OS:  
`config`  
`delete system login banner post-login`  
`commit`  
`save`  

In the distribution Switch (Exos):  
`configure banner after-login`  
`<blank>`  
`<blank>`  



In linux devices:  
`sudo rm /etc/motd`  




In Windows devices, enter Ctrl+R and `secpol` to search and open the Local Security Policy.  
Under Local Policies > Security Options  
Look for `Interactive login: Message text` and `Interactive: Message title`. Remove the contents and press ‘ok’.  
