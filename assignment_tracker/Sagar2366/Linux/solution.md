# Linux and Shell Scripting

## 1. Create free trial account on all 3 cloud providers - AWS, GCP, AZURE

![](./Images/aws.png)
![](./Images/azure.png)
![](./Images/gcp.png)

## 2. Blog on Operating system, Architecture, OS Features

### ![Exploring the Heart of Computing: A Deep Dive into Operating System Architecture and Features](https://souravk.hashnode.dev/os)

## 3. Blog on Linux, Linux for DevOps

### ![Linux for DevOps: What You Need to Know](https://souravk.hashnode.dev/linux-for-devops)

## 4. Launch instance in cloud provider Azure, AWS, GCP

### AWS
![](./Images//aws-vm.png)

### Azure
![](./images/azure-vm.png)

### GCP
![](./images/gcp-vm.png)


## 5. Blog on VI editor - modes and shortcuts

### ![How to Use Vim](https://souravk.hashnode.dev/how-to-use-vim)

## 6. Blog on Linux filesystem and hierarchy

### ![]()

## 7. Blog on SSH and SCP

### ![]()

## 8. Connect remote machine/instance using SSH Azure, AWS, GCP

### AWS
![](./images/ssh-aws-command.png)
![](./images/ssh-aws.png)

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

uptime_seconds=$(cut -d. -f1 /proc/uptime)

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

total_memory=$(free -m | awk '/Mem:/ {print $2}')

free_memory=$(free -m | awk '/Mem:/ {print $4}')

available_memory=$(free -m | awk '/Mem:/ {print $7}')

echo "Total Memory: $total_memory MB"
echo "Free Memory: $free_memory MB"
echo "Available Memory: $available_memory MB"
```
## 15. Shell script to check if Disk usage is more than 75% then send an email report
```

```
## 16. Shell script and run it in background
## 17. Shell script to verify if password is expired or how many days left for password to get expired