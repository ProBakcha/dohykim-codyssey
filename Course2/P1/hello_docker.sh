docker run hello-world
docker images
docker inspect hello-world
docker ps -a
docker inspect $(docker ps -aq --filter "ancestor=hello-world")
docker history hello-world
docker rm $(docker ps -aq --filter "ancestor=hello-world")
docker rmi hello-world
