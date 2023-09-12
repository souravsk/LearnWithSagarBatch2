terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    bucket = "mybucketec2tfstate"
    key    = "ec2terraformstate"
    region = "eu-central-1"
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "eu-central-1"
}

resource "aws_key_pair" "keypair" {
  key_name   = var.key_name
  public_key = ""  ## ssh-keygen
}

resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = var.instance_type
  tags = {
    Name = "HelloWorld"
  }
  key_name = aws_key_pair.keypair.key_name
}

output "aws_instance_public_ip" {
  value = aws_instance.web.public_ip
}
