terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "3.0.2"
    }
  }
}


provider "docker" {
  host = "unix:///Users/sutekar/.docker/run/docker.sock"
}

resource "docker_image" "flaskrestapitf" {
  name = "flaskrestapitf"
  build {
    context = "."
  }
}

resource "docker_container" "flaskrestapitf" {
  name  = "flaskrestapitf"
  image = docker_image.flaskrestapitf.image_id
}

output "container_name" {
  value = docker_container.flaskrestapitf.command
}
