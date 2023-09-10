

variable "ami_id" {
  type = string
  default = "ami-04e601abe3e1a910f"
}

variable "instance_type" {
  type = string
  default = "t2.micro"
}

variable "key_name" {
  type = string
  default = "ssh-key"
}
