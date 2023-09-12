# Linux and Shell Scripting Solutions

## 1. Create free trial account on all 3 cloud providers - AWS, GCP, AZURE
![](./images/aws.png)
![](./images/azure.png)
![](./images/gcp.png)

## 2. Blog on Operating system, Architecture, OS Features

### [Exploring the Heart of Computing: A Deep Dive into Operating System Architecture and Features](https://souravk.hashnode.dev/os)

## 3. Blog on Linux, Linux for DevOps

### [Linux for DevOps: What You Need to Know](https://souravk.hashnode.dev/linux-for-devops)

## 4. Launch instance in cloud provider Azure, AWS, GCP

### AWS
![](./images//aws-vm.png)

### Azure
![](./images/azure-vm.png)

### GCP
![](./images/gcp-vm.png)


## 5. Blog on VI editor - modes and shortcuts

### [How to Use Vim](https://souravk.hashnode.dev/how-to-use-vim)

## 6. Blog on Linux filesystem and hierarchy

### [Linux File System](https://souravk.hashnode.dev/linux-file-system)

## 7. Blog on SSH and SCP

### [what are SSH and SCP?](https://souravk.hashnode.dev/ssh-scp)

## 8. Connect remote machine/instance using SSH Azure, AWS, GCP

### AWS
![](./images/ssh-aws-command.png)
![](./images/ssh-aws.png``)

### Azure
![](./images/ssh-azure-command.png)
![](./images/ssh-azure.png)

### GCP
![](./images/ssh-gcp-command.png)
![](./images/ssh-gcp.png)

## 9. Copy a local file to remote instance using SCP Azure, AWS, GCP

### AWS
![](./images/L-R-AWS-command.png)
![](./images/L-R-AWS-output.png)

### Azure
![](./images/L-R-Azure-output.png)

### GCP
![](./images/L-R-GCP-command.png)
![](./images/L-R-GCP-output.png)

## 10. Copy a file from remote machine to local machine Azure, AWS, GCP

### AWS
![](./images/R-L-AWS-command.png)
![](./images/R-L-AWS-output.png)

### Azure
![](./images/R-L-Azure-command.png)
![](./images/R-L-Azure-output.png)

### GCP
![](./images/%20R-L-GCP-command.png)

## 11. Copy a file from one instance to another remote instance Azure, AWS, GCP

### First Local system to GCP Server
![](./images/L-gcp-comand.png)
![](./images/gcp-output.png)

### then from GCP to Azure
![](./images/gcp-azure-command.png)
![](./images/azure-output.png)

### then from Azure to AWS
![](./images/azure-aws-comand.png)
![](./images/aws-output.png)

## 12. Shell script to find the Linux Operating system
```
#!/bin/bash

os_name=$(uname -s)
os_release=$(uname -r)

echo "Operating System: $os_name"
echo "Kernel Release: $os_release"

```
## 13. Shell script to restart the system if instance has been up for 2 weeks
```
#!/bin/bash
: 'This line retrieves the system's uptime in seconds. 
    The command /proc/uptime provides a number that represents the system's uptime in seconds, including fractions of a second. 
    The cut command is used to extract the whole number part (seconds) by splitting the output at the decimal point and taking the first part (-f1). 
    The result is stored in the uptime_seconds variable.
'
uptime_seconds=$(cat /proc/uptime | awk -F'.' '{print $1}')

#(2 weeks = 1209600 seconds)
max_uptime=1209600

if [ "$uptime_seconds" -gt "$max_uptime" ]; then
    echo "System has been up for more than 2 weeks. Restarting..."
    sudo reboot
else
    echo "System uptime is within acceptable range."
fi

```
## 14. Shell script to get total, free and available memory
```
#!/bin/bash

:   '
        `free` is use to Display amount of free and used memory in the system
        -g it how the memory size in GB
        awk is file process command which help as to get the data from file


'
total_memory=$(free -g | awk '/Mem:/ {print $2}')

free_memory=$(free -g | awk '/Mem:/ {print $4}')

available_memory=$(free -g | awk '/Mem:/ {print $7}')

echo "Total Memory: $total_memory MB"
echo "Free Memory: $free_memory MB"
echo "Available Memory: $available_memory MB"
```
## 15. Shell script to check if Disk usage is more than 75% then send an email report
```
#!/bin/bash

: '
    df displays free disk space
    NR will get the row and $5 will get the column
    cut will remove the %
'

disk_limit=75

# Get current disk usage
disk_usage=$(df -h | awk 'NR == 2 {print $5}' | cut -d% -f1)

# Check if disk usage is greater than the limit
if [ "$disk_usage" -gt "$disk_limit" ]; then
    subject="Disk Usage Alert"
    message="Disk usage is currently at $disk_usage% which is above the threshold of $disk_limit%."
    echo "$message" | mail -s "$subject" souravk326@gmail.com
else
    # Disk usage is within limits
    echo "Disk usage is within acceptable range."
fi

```
## 16. Shell script and run it in background
```
sleep 10

```
## 17. Shell script to verify if password is expired or how many days left for password to get expired
```
#!/bin/bash

username=$(whoami)
expiration_days=$(sudo chage -l "$username" | awk 'NR == 7 {print $10}')

if [ "$expiration_days" -gt 0 ]; then
    sudo chage -l "$username" | awk 'NR == 7'
else
    echo "Password is expired"
fi

```
## 18. Blog and practice to add new user into EC2 instance - Additional operations : Delete user, change group for the user, change the permissions for the user, etc

### [Create User In Ubuntu](https://souravk.hashnode.dev/create-user-in-ubuntu)

## 19. Blog on Journalctl and system logging

### [Journalctl and system logging](https://souravk.hashnode.dev/journalctl-and-system-logging)

## 20. Blog on File and directory commands

### [Linux Commands](https://souravk.hashnode.dev/linux-commands)

## 21. Blog on Chomod and chown command, ACL

### [Mastering File Permissions: Exploring chmod, chown, and ACL Commands](https://souravk.hashnode.dev/chmod-chown-acl)

## 22. Shell script to connect different instances and add cron entry to stop instances every night at 11 PM (Cronjob)
```


```

## 23. Shell script to cleanup filesystem using cron
```


```
## 24. Shell script to take a backup of instance volumes/drives
```


```
## 25. Blog and practical on wget and curl command

### [What is wget and curl command?](https://souravk.hashnode.dev/wget-curl)

## 26. Connect to web server using CURL and perform GET/POST/PUT/DELETE/UPDATE (CRUD) operations.
    a. Connect to AWS using REST API and use curl to get a list of instance which are not running. Additionally, once you get a list terminate those instance.
    COMING SOON
```


```
## 28. Blog on NMTUI - set static IP address, hostname, dns of instance
   a. Azure
   b. AWS
   C. GCP
   D. Local

```



```
## 29. Blog on file/directory compression and extraction with practical
```


```
## 30. Shell script to find files+directories which have more than 1GB in size, and send a report via email

```



```
## 31. Shell script to find files which have permission provided by the user as input
```


```
## 32. Blog to create your own Linux command + practical
## 33. Shell script to manage instances - (Create, terminate, Stop)
   a. Azure
   b. AWS
   C. GCP
## 34. System status project with top and /proc/meminfo + /proc/cpuinfo command
## 35. Send email report only if
   ### a. CPU usage of the process is more than 70%
   ```
   
   
   ```
   b. Memory usage of the process is more than 75%
## 36. COPY system_program files (zip,tar) into remote machine and set a cron job to run the program at twice in a day