## MONITORING USING PROMETHEUS AND GRAFANA


## What is Prometheus?
Prometheus is an open-source systems monitoring and alerting toolkit originally built at SoundCloud. 
Since its inception in 2012, many companies and organizations have adopted Prometheus, and the project has a very active developer and user community. 
It is now a standalone open source project and maintained independently of any company. 
Prometheus joined the Cloud Native Computing Foundation in 2016 as the second hosted project, after Kubernetes.
Prometheus collects and stores its metrics as time series data, i.e. metrics information is stored with the timestamp at which it was recorded, 
alongside optional key-value pairs called labels. Grafana is an open-source platform for monitoring and observability. 
It allows you to query, visualize, alert on and understand your metrics no matter where they are stored.


## What is Grafana?
Grafana is open source visualization and analytics software. 
It allows you to query, visualize, alert on, and explore your metrics no matter where they are stored. 
In plain English, it provides you with tools to turn your time-series database (TSDB) data into beautiful graphs and visualizations.


We will use Helm to install and manage Prometheus and Grafana on AKS cluster.

## Steps to be followed
```
Install Prometheus and Grafana using Helm
Setup Port-forwarding for both Prometheus and Grafana
Create a Service Principal and add roles to AKS cluster RG
Create Data Source in Grafana
Import Azure Monitor for Containers in Grafana
View the metrics in Grafana Dashboard
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
```

In order to login to the Grafana dashboard, username and password are required which can be retrieved by using the below command:
# Get the Username
kubectl get secret -n prometheus prometheus-grafana -o=jsonpath='{.data.admin-user}' |base64 -d
# Get the Password
kubectl get secret -n prometheus prometheus-grafana -o=jsonpath='{.data.admin-password}' |base64 -d

## Configure data source and dashboards


