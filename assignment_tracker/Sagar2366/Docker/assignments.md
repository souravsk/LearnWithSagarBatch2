

1. Blog on Containerisation & Docker - why, what, how ?
2. Docker containers and images
3. Write Hello world webapp  in Python
4. Dockerise Hello World webapp
5. Push docker image to Docker Hub
6. Deploy nginx server and configure SSL
7. REST API using Flask/Python + MongoDB or preferrable language
   a. Locally - Run mongoDB, set environment variable MONGODB_ENDPOINT, run your python application
   b. Docker :
       - create user defined bridge network - docker network create flaskmongo
       - run mongo container and use user defined bridge network ->>  docker run -itd -p 27017:27017 --name mongo --network flaskmongo -e MONGO_INITDB_DATABASE=example mongo:4.0.4
       - Build Docker image for flask container
       - Run flask container and use user defined bridge network ->> docker run -itd --name flaskrest --network flaskmongo -p 5060:5000 flaskrestapi\
       - Access your application on ->> http://localhost:5060/items
   c. Docker Compose -
       - To build only docker images ->> docker compose build
       - Start docker compose application ->>  docker compose up -d
       - Access your application on ->> http://localhost:5060/
   d. Kubernetes
       - Namespace
       - Mongo, flask POD using Deployment
       - Services for Mongo and Flask
       - MongoDB PV, PVC
       kubectl apply -f kubernetes/.
       kubernetes delete -f kubernetes/.
9. 

EXTRA SESSIONS -
1. DOCKER REST API
2. PODMAN
3. CRI-O
4. Python
5. Optimising Docker image sizes
6. Shell scripting
7. Portfolio
8. Docker Swarm & networking
9. Share code to connect MongoDB Atlas from Python

REFERENCES -
1. Docker installation : https://docs.docker.com/desktop/install/
2. Dockerfile : https://docs.docker.com/engine/reference/
3. Kubernetes TOOLS : https://kubernetes.io/docs/tasks/tools/



Debugging steps :
1. Minikube image pull error -
   Set docker to point to minikube :
   eval $(minikube docker-env)

  Push to minikube docker -
  docker build -t hello-node:v1 .
  
  Set your deployment to not pull IfNotPresent
  K8S default is set to "Always" Change to "IfNotPresent"
  imagePullPolicy: IfNotPresent


