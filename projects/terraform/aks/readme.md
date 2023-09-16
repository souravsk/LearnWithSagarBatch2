Assignments -
1. Setup Azure provider
2. Configure Azure auth (try diff ways)
3. Create modules for
   resource group
   virtual network
   subnet
   AKS
   Azure Virtual Machine
   EKS
   GKE
   IAM users
5. Refer to previously created module in child module
   For AKS - refer resource group, vnet, subnet modules
7. Take inputs from user
8. Show important values as output, use sensitive attribute in output block
9. Deploy previously created Docker, and Kubernetes projects on newly created clusters
10. Add Azure monitoring and alerting for AKS cluster
   
Links -
Azure provider - https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs
Azure authentication - https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/service_principal_client_secret


