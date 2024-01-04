#This script is to test FTP server

import subprocess
import time

# Install pyftpdlib
subprocess.run(["pip3", "install", "pyftpdlib"])

# Start FTP server with username and password
server_process = subprocess.Popen(["python3", "-m", "pyftpdlib", "-w", "--user=username", "--password=password"])

# Give some time for the server to start (adjust as needed)
time.sleep(5)

# Transfer files using WinSCP
#Adjust the placeholders (username, password, hostname, local_path, remote_path) with your actual server and file paths
winscp_command = f"winscp.exe sftp://username:password@hostname/ -rawsettings Compression=0 -rawsettings ProxyMethod=0 -resumesupport=on -delete -nopreservetime -nopermissions -transfer=binary -criteria=time -passive=off -explicitssl -certificate=\"\" -filemask=\"*<2D -resumesupport=off\" -resumesupport=on -delete -nopreservetime -nopermissions -transfer=binary -criteria=time -passive=off -explicitssl -certificate=\"\" -filemask=\"*<2D -resumesupport=off\" \"local_path\" \"/remote_path\""

winscp_process = subprocess.Popen(winscp_command, shell=True)
winscp_process.wait()

# Terminate the FTP server process
server_process.terminate()
