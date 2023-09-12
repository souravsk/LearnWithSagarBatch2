## Below are some of the benefits of using Terraform.

```
Does orchestration, not just configuration management
Supports multiple providers such as AWS, Azure, GCP, DigitalOcean and many more
Provide immutable infrastructure where configuration changes smoothly
Uses easy to understand language, HCL (HashiCorp configuration language)
Easily portable to any other provider
Supports Client only architecture, so no need for additional configuration management on a server
```

## Terraform Core concepts
Below are the core concepts/terminologies used in Terraform:
```
Variables: Also used as input-variables, it is key-value pair used by Terraform modules to allow customization.
Provider: It is a plugin to interact with APIs of service and access its related resources.
Module: It is a folder with Terraform templates where all the configurations are defined
State: It consists of cached information about the infrastructure managed by Terraform and the related configurations.
Resources: It refers to a block of one or more infrastructure objects (compute instances, virtual networks, etc.), which are used in configuring and managing the infrastructure.
Data Source: It is implemented by providers to return information on external objects to terraform.
Output Values: These are return values of a terraform module that can be used by other configurations.
Plan: It is one of the stages where it determines what needs to be created, updated, or destroyed to move from real/current state of the infrastructure to the desired state.
Apply: It is one of the stages where it applies the changes real/current state of the infrastructure in order to move to the desired state.
```

## Terraform Lifecycle
Terraform lifecycle consists of – init, plan, apply, and destroy.

terraform lifecycle -
```
Terraform init initializes the working directory which consists of all the configuration files
Terraform plan is used to create an execution plan to reach a desired state of the infrastructure. Changes in the configuration files are done in order to achieve the desired state.
Terraform apply then makes the changes in the infrastructure as defined in the plan, and the infrastructure comes to the desired state.
Terraform destroy is used to delete all the old infrastructure resources, which are marked tainted after the apply phase.
```

## How Terraform Works?
Terraform has two main components that make up its architecture:

## Terraform Core
Providers
terraform architecture - geekflare
Terraform Core
Terraform core uses two input sources to do its job.

The first input source is a Terraform configuration that you, as a user, configure. Here, you define what needs to be created or provisioned. 
And the second input source is a state where terraform keeps the up-to-date state of how the current set up of the infrastructure looks like.

So, what terraform core does is it takes the input, and it figures out the plan of what needs to be done. 
It compares the state, what is the current state, and what is the configuration that you desire in the end result. 
It figures out what needs to be done to get to that desired state in the configuration file. It figures what needs to be created, what needs to be updated, what needs to be deleted to create and provision the infrastructure.

## Providers
The second component of the architecture are providers for specific technologies. This could be cloud providers like AWS, Azure, GCP, or other infrastructure as a service platform. It is also a provider for more high-level components like Kubernetes or other platform-as-a-service tools, even some software as a self-service tool.

It gives you the possibility to create infrastructure on different levels.

For example – create an AWS infrastructure, then deploy Kubernetes on top of it and then create services/components inside that Kubernetes cluster.

Terraform has over a hundred providers for different technologies, and each provider then gives terraform user access to its resources. So through AWS provider, for example, you have access to hundreds of AWS resources like EC2 instances, the AWS users, etc. With Kubernetes provider, you access to commodities, resources like services and deployments and namespaces, etc.

So, this is how Terraform works, and this way, it tries to help you provision and cover the complete application setup from infrastructure all the way to the application.

Let’s do some practical stuff. 👨‍💻

We will install Terraform on Ubuntu and provision a very basic infrastructure.

## Install Terraform
```
Download the latest terraform package.

Refer to the official download page to get the latest version for the respective OS.
```
