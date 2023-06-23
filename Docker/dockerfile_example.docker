FROM mcr.microsoft.com/dotnet/core/aspnet:3.1   #base image for dockerfile upon which apps will be built on
RUN mkdir /app  #create a dir named /app inside container image
WORKDIR /app    #set working directory for subsequent instructions in dockerfile
COPY ./webapp/bin/Release/netcoreapp3.1/publish ./  #copy compiled application from local directory into container image
COPY ./config.sh/ ./    #copy config file
RUN bash config.sh  #execute the script using run
EXPOSE 80 #application running in the container is listening on this port
ENTRYPOINT ["dotnet","webapp.dll"]  #which binary or script to start when container is started Syntax: ENTRYPOINT["command_to_run", "parameters"] Note: webapp.dll is a file copied into current directory from locally compiled app.



#RUN this dockerfile using:
#docker build -t webappimage:v1 .
# -t is used to specify "container_image_name:version_tag" to our application: In this case, "webappimage:v1"