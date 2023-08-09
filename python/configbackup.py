import os
import paramiko
from datetime import datetime
from netmiko import ConnectHandler

#define devices
devices = [
    {
        'device_type': 'vyos',
        'ip': '10.10.1.1',
        'username': 'vyos',
        'password': 'vyos',
        'port': 22,
    },
    {
        'device_type': 'vyos',
        'ip': '10.10.1.2',
        'username': 'vyos',
        'password': 'vyos',
        'port': 22,
    },
    {
        'device_type': 'extreme_exos',
        'ip': '10.10.2.2',
        'username': 'ansible',
        'password': 'ansible',
        'port': 22,
    }
]

backup_folder = '/home/student/backups'

#create backup folder if it doesn't exist
if not os.path.exists(backup_folder):
    os.makedirs(backup_folder)

def backup_config(device):
    try:
        #connect to device
        net_connect = ConnectHandler(**device)
        hostname = net_connect.find_prompt().replace("#", "")

        #get configuration
        output = net_connect.send_command('show configuration')

        #save configuration to file
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{hostname}_{timestamp}_config.txt"
        local_filepath = os.path.join(backup_folder, filename)
        with open(local_filepath, 'w') as f:
            f.write(output)

        #define storage server details
        storage_server_ip = '10.10.16.10'
        storage_server_username = 'student'
        storage_server_password = 'P@ssw0rd'
        storage_server_filepath = f'{backup_folder}/{filename}'

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(storage_server_ip, username=storage_server_username, password=storage_server_password)

        #create backup folder on storage server if it doesn't exist
        stdin, stdout, stderr = ssh_client.exec_command(f'mkdir -p  {backup_folder}')
        stdout.channel.recv_exit_status()

        with open(local_filepath, 'rb') as local_file:
            ftp_client = ssh_client.open_sftp()
            ftp_client.putfo(local_file, storage_server_filepath)
            ftp_client.close()

        ssh_client.close()
        print(f"Configuration for {hostname} backed up successfully.")

    except Exception as e:
        print(f"FAILED: backup configration for {hostname}. Error: {str(e)}")

    finally:
        if 'net_connect' in locals():
            #disconnect from device
            net_connect.disconnect()

#backup configurations for each device listed
for device in devices:
    backup_config(device)
