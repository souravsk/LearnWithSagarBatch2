## MONITORING USING PROMETHEUS AND GRAFANA

Kubernetes has become a platform of choice for building cloud native applications. Kubernetes is highly scalable, highly available, and easy to use, 
and has many other advantages that make it an excellent choice for building distributed applications.
However, its distributed nature means monitoring everything that is happening within the cluster can be a challenge. Prometheus and Grafana make our experience better.
We will set up a Kubernetes cluster using Azure Kubernetes Service (AKS) and deploy Prometheus and Grafana to gather monitoring data and visualize them.

 

## Understand the tooling
## Prerequisites
We will be creating a Kubernetes cluster using Azure Kubernetes Service (AKS), you will need an Azure account, the Azure CLI, Kubectl and Helm.
Azure account
Azure CLI
Kubectl
Helm

## Create an Azure Kubernetes Service (AKS) Cluster
Sign into the Azure CLI by running the login command.

```
az login
```

# Install or update kubectl.

```
az aks install-cli
```

# Create two bash/zsh variables which we will use in subsequent commands. You may change the syntax below if you are using another shell.

```
RESOURCE_GROUP=aks-prometheus
AKS_NAME=aks1
```

# Create a resource group. We have chosen to create this in the eastus Azure region.
```
az group create --name $RESOURCE_GROUP --location eastus
```

# Create a new AKS cluster using the az aks create command. Here we create a 3 node cluster using the B-series Burstable VM type which is cost-effective and suitable for small test/dev workloads such as this.

``` az aks create --resource-group $RESOURCE_GROUP \
  --name $AKS_NAME \
  --node-count 3 \
  --node-vm-size Standard_B2s \
  --generate-ssh-keys
```

This may take a few minutes to complete.

# Authenticate to the cluster we have just created.

```
az aks get-credentials \
  --resource-group $RESOURCE_GROUP \
  --name $AKS_NAME
```

# We can now access our Kubernetes cluster with kubectl. Use kubectl to see the nodes we have just created.

``` kubectl get nodes
```

 
You will be able to install the latest versions of Kubectl and Helm using the Azure CLI, or install them manually if you prefer.

## What is Prometheus?
Prometheus is an open-source systems monitoring and alerting toolkit originally built at SoundCloud. 
Since its inception in 2012, many companies and organizations have adopted Prometheus, and the project has a very active developer and user community. 
It is now a standalone open source project and maintained independently of any company. 
Prometheus joined the Cloud Native Computing Foundation in 2016 as the second hosted project, after Kubernetes.
Prometheus collects and stores its metrics as time series data, i.e. metrics information is stored with the timestamp at which it was recorded, 
alongside optional key-value pairs called labels.
Prometheus uses an exporter architecture. Exporters are APIs that may collect or receive raw metrics from a service and expose them in a specific format that Prometheus consumes.
Once Prometheus discovers a new exporter (or if you configure one), it will start collecting metrics from these services and store them in persistent storage.

## What is Grafana?
Grafana is open source visualization and analytics software. 
It allows you to query, visualize, alert on, and explore your metrics no matter where they are stored. 
In plain English, it provides you with tools to turn your time-series database (TSDB) data into beautiful graphs and visualizations.


We will use Helm to install and manage Prometheus and Grafana on AKS cluster.

## Is helm installed?
We will use helm to install Prometheus & Grafana monitoring tools for this chapter. Please review installing helm chapter for instructions if you don’t have it installed.

# add prometheus Helm repo
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

# add grafana Helm repo
helm repo add grafana https://grafana.github.io/helm-charts

## Steps to be followed
```
Install Prometheus and Grafana using Helm
Setup Port-forwarding for both Prometheus and Grafana
Create a Service Principal and add roles to AKS cluster RG
Create Data Source and dashboard in Grafana
View the metrics in Grafana Dashboard

```

Install Prometheus and Grafana
# Define public Kubernetes chart repository in the Helm configuration
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
# Update local repositories
helm repo update
# Search for newly installed repositories
helm repo list
# Create a namespace for Prometheus and Grafana resources
kubectl create ns prometheus
# Install Prometheus using HELM
helm install prometheus prometheus-community/kube-prometheus-stack -n prometheus
# Check all resources in Prometheus Namespace
kubectl get all -n prometheus


In order to login to the Grafana dashboard, username and password are required which can be retrieved by using the below command:
# Get the Username
kubectl get secret -n prometheus prometheus-grafana -o=jsonpath='{.data.admin-user}' |base64 -d
# Get the Password
kubectl get secret -n prometheus prometheus-grafana -o=jsonpath='{.data.admin-password}' |base64 -d

## Configure data source and dashboards


