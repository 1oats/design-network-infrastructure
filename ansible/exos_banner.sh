#!/bin/bash

# Read the banner content from files/banner.txt
BANNER_CONTENT=$(<files/banner.txt)

# Connect to the EXOS switch and send configuration commands using HEREDOC
sshpass -p "ansible" ssh -T ansible@10.10.2.2 << EOF
configure banner after-login 
"$BANNER_CONTENT"

save
y
exit
exit
EOF
