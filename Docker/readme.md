1. Installing docker on Ubuntu (https://docs.docker.com/engine/install/ubuntu/)
- Update the apt package index and install packages to allow apt to use a repository over HTTPS:
  - sudo apt-get update 
  - sudo apt-get install ca-certificates curl gnupg
- Add Docker’s official GPG key:
   -  sudo install -m 0755 -d /etc/apt/keyrings
   - curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
   - sudo chmod a+r /etc/apt/keyrings/docker.gpg
- Use the following command to set up the repository:
   - echo \
     "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
     "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
     sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
- Install Docker Engine
   Update the apt package index:
     - sudo apt-get update
   To install the latest version, run:
     - sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
   Verify that the Docker Engine installation is successful by running the hello-world image.:
     - sudo service docker start 
     - sudo docker run hello-world
2. Docker commands
    - Common Commands:
      run    :      Create and run a new container from an image
      exec   :     Execute a command in a running container
      ps     :     List containers
      build  :     Build an image from a Dockerfile
      pull   :     Download an image from a registry
      push   :     Upload an image to a registry
      images :     List images
      login  :     Log in to a registry
      logout :     Log out from a registry
      search :     Search Docker Hub for images
      version:     Show the Docker version information
      info   :     Display system-wide information

   - docker image ls: list of all images present locally.
   - docker ps: list of running images(containers)
   - docker stop "appname"
   - docker rm "appname"
