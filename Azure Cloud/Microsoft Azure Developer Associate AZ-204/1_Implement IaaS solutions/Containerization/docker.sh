# Create a container image using docker for dotnetcore application
# first build and run the dotnet app
dotnet build ./webapp
dotnet run --project ./webapp
curl http://localhost:5000 # check if working
# then, publish local dotnet build
dotnet publish -c Release ./webapp
# Docker Build the container and tag it
docker build -t webappimage:v1 # using the dockerfile found in /Linux/Docker/Dockerfile in this repo.
# to see the output to console:
docker build --progress plain -t webappimage:v1
# To clean up images and image cache:
docker rmi webappimage:v1 && docker builder prune --force && docker image prune --force
# Run and test container locally
docker run --name webapp --publish 8080:80 --detach webappimage:v1
curl http://localhost:8080
# Stop and delete container
docker stop webapp
docker rm webapp
