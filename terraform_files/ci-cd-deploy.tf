# Configure the provider
provider "null" {
  state = true
}

# Set variables
variable "gitlab_container_registry_url" {
  type        = string
  description = "URL of the GitLab Container Registry"
}

variable "gitlab_username" {
  type        = string
  description = "Username for authentication with the GitLab Container Registry"
}

variable "gitlab_password" {
  type        = string
  description = "Password for authentication with the GitLab Container Registry"
}

variable "image_name" {
  type        = string
  description = "Name of the image to deploy"
}

# Deploy the container image
resource "null_resource" "deploy_image" {
  connection {
    type        = "ssh"
    host        = "your-local-machine-ip-or-hostname"
    user        = "your-ssh-username"
    private_key = file("~/.ssh/your-private-key.pem")
  }

  provisioner "local-exec" {
    command = "docker run -d --rm ${var.gitlab_container_registry_url}/${var.image_name}"
  }
}
