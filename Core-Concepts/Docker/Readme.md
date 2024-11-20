## INTRODUCTION :

![image](https://github.com/user-attachments/assets/5b42deeb-c0ec-4f06-8257-6d4321a30c81)

### **Containerization:**


- It is a lightweight virtualization technology alternative to hypervisor virtualization.
- Any application can be bundled in a container can run without any worries about dependencies, libraries and binaries.
- So, containers are designed to run on physical servers, virtual machines and any cloud instances.
- Also container was designed to solve modern problems and application management issues. so it is not a replacement for virtualization, but it’s complementary to it.
  
    
#### » Cgroups (Control Groups)
    
**Cgroups** (Control Groups) is a Linux kernel feature for limiting, accounting, and isolating the resource usage (CPU, memory, disk I/O, etc.) of a group of processes. It helps allocate resources among user-defined groups efficiently and ensures that one group's resource usage doesn't adversely affect others.
    
#### » Namespaces
    
**Namespaces** are a Linux kernel feature that provides isolated environments for processes. Each namespace has its own global system resources (process IDs, network interfaces, file system mounts, etc.), ensuring that processes in different namespaces do not interfere with each other. This isolation is essential for containerization, allowing multiple containers to run on the same host without conflicts.
    
#### » OverlayFS
    
**OverlayFS** (Overlay Filesystem) is a union mount filesystem implementation in Linux that allows multiple filesystems to be stacked on top of one another, creating a single, unified view. It's often used in containerization platforms like Docker to provide a writable layer on top of a read-only base filesystem.
    
---

### Docker :

![image](https://github.com/user-attachments/assets/61002ea3-2842-47f1-8635-fb22111d2941)

It is an open-source platform tool designed to manage the containers, which allows us to build the application in a container with required libraries, binaries, dependencies to run the application, ship the container and run anywhere.

- Virtualization Software for containers
- Makes developing and deploying applications easier.
- Packages application with all the necessary dependencies, configuration, system tools and runtime [environment configuration]. (A standardized unit that has everything the application needs to run )
- Portable artifact , easily shared and distributed.

**Why do we use docker ?**
```
    - Portability
    - Light weight
    - Fast delivery and scalable
    - continous deployment and testing
    - Resource optimization
    - Multiple OS on single host
```
```
  📌 Docker standardizes process of running any service on any environment.
     Same command for all OS. Easy to run different versions of same app without any conflicts.
```


**Difference between VM and Docker :**
    
<img src="https://github.com/user-attachments/assets/f1f9e23b-236d-4541-919a-468942465dae" alt="description" width="500" />


    
**Docker**
  ```  
    -  Image Size: A couple of MB
    -  Startup Time: Containers take seconds to start
    -  Compatibility: Compatible with Linux distros
    -  Requirements: No boot loader and kernel needed
```
    
**Virtual Machine**
 ``` 
    -  Image Size: A couple of GB
    -  Startup Time: VMs take minutes to start
    -  Compatibility: Compatible with all OS
    -  Requirements: Full OS needs kernel, boot loader, systemd
```

 **📌 Docker Compatibility issues : [ Reason ]**

- Linux based docker images cannot use windows kernel
- Most conatiners are linux based.
- Orginally built for LInux Os.

**Solution:** 

- Allows you to run linux containers on windows or Mac Os
- It uses a hypervisor layer with a lightweight linux distro

---

**Docker Desktop :**
    
![image](https://github.com/user-attachments/assets/113bda3f-f100-483a-961a-90552f1eb78d)

<br> 

**Docker Engine** is the core component of the Docker platform, responsible for building, running, and managing containers. It provides an environment where containers can be created, deployed, and executed on a host system.
    
    - A server with long-running deamon process “dockerd”.
    - Manage images & containers.
    
 <br>  
 
**Docker CLI - Client :**
    
    - CLI (”Docker”)  to interact with docker server
    - execute docker commands to start/stop… containers.
    
<br>    

**GUI Client :**
    
    - To manage your conatiners and images with a graphical user interface.
<br> 
    
**Docker Architecture :**
    
  ![image](https://github.com/user-attachments/assets/eb1be850-a97d-4aef-8270-7418b35131c5)
  
---
    
**Docker Essentials :**

1. **Docker Images :**
       
    - An executable application artifact.
    - Includes app source code, but also complete environment configuration.
    - It is a template for a docker containers and it is very similar to snapshot image with smaller in size.
    - single image can used to create multiple containers.
    - Docker images are consists of many layers with unique image ID from base image.each layer have some changes commited on top of a existing layer.
    
    ![image](https://github.com/user-attachments/assets/5446b5a9-8ebe-4f18-9e1b-5d661235be35)

2. **Docker Containers :** 
    
    - A running instance of an image.
    - A docker container image is a lightweight, standalone,executable package of software that includes everything needed to run an application.
    - A container is a instance of container image with required dependencies installed

     <br>
     
    ```
    📌 Note :  A container run only if there is any service running or else it will stop.
    ```

    
3.**Docker Registry :**
    
  - A storage and distribution system for docker images.
  - Official images are maintained by the software authors or in collobration with the Docker community.
  - Docker hosts the one of the biggest Docker Registry called Dockerhub - Find and share docker images.
  - official images available for applications like Redis, Mongodb, Postgres etc..

  ➜ Docker Hub: https://hub.docker.com/
    
4. **Image versioning :**
    
  - Docker images are versioned **eg:** `redis:6.1` , `redis:6.2`
  - Different versions are identified by tags. Latest tag means the images based on latest release.
    
 ### Docker Essential Commands :
    
    ## General Information:
    
    $ sudo docker -v                   # Show version of Docker
    $ docker info                      # Display system-wide information
    $ docker system df                 # Show Docker disk usage
    $ sudo docker system events        # Show logs or errors if there's a problem with Docker or it crashed
    $ docker <command> help            # Show usage of a specific command
    $ docker inspect <container-name>  # Return low-level information on Docker objects
  
    ## Image Management:
    
    $ docker search <imagename>                # Search for an image on Docker Hub
    $ docker images                            # List all images on the local system
    $ docker pull <imagename>                  # Pull an image from a registry
    $ docker rmi <image-name>                  # Remove an image
    $ docker build -t username/imagename:tag   # Build an image from a Dockerfile
    $ docker push <imagename>                  # Push an image to a registry
    $ docker login                             # Log in to a Docker registry
    
    ## Container Management:
    
    $ docker ps                                                                 # List running containers
    $ docker ps -a                                                              # List all containers, including stopped ones
    $ docker run --name <container-name> -d <imagename>                         # Run a container in detached mode
    $ docker run --name <container-name> -e APP-API=1234 -d <imagename>         # Run a container with environment variables
    $ docker run --name <container-name> -p localhost:dockerhost -d <imagename> # Run a container with port mapping
    $ docker exec -it <container-name> /bin/sh                                  # Open an interactive terminal in the container using sh
    $ docker exec -it <container-name> /bin/bash                                # Open an interactive terminal in the container using bash
    $ docker exec <container-name> <command>                                    # Execute a command inside a container without logging in
    $ docker cp <source from local system> <container-name or id:/destination>  # Copy files from local system to container
    $ docker start <container-name or id>                                       # Start a stopped container
    $ docker stop <container-name or id>                                        # Stop a running container
    $ docker rm <container-name>                                                # Remove a container
    $ docker stats                                                              # Display a live stream of container resource usage statistics
    $ docker logs <container-name>                                              # Fetch logs of a container
    $ docker container prune                                                    # Remove all stopped containers
  
    
**Docker files :**
  - **Dockerfiles** are text files that list instructions for the Docker daemon to follow when building a Docker image.
  - Used to create custom images for your application.
    
**Structure of Dockerfile:**
---
    
#### Base Image:
    
  - Dockerfiles start from a parent image or "base image".
  - It is a Docker image that your image is based on, the starting point of creating a containerized application.
  - Contains minimal OS and runtime components needed.
  - On top of that, we add your application code and dependencies to create a customized Docker image.

1. **FROM**:
    - Dockerfile must start with a `FROM` instruction.
    - Build this image from the specified image.
      <br>
      
    ```docker
    FROM NODE:19-ALPINE
    ```
    
2. **COPY**:
    - Adds files and folders to your image filesystem (src to dest).
    <br>
    
    ```docker
    COPY main.js /app/main.js
    ```
    
3. **RUN**:
    - This command runs a command inside the image you are building. It creates a new image layer on top of the previous one; it will contain the filesystem changes the command applies.
    <br>
    
    ```docker
    RUN pip install -r requirements.txt
    ```
    
4. **ADD**:
     - Similar to copy but additionally supports remote file URLs and automatic archive extraction.
    <br>
    
    ```docker
    ADD <http://example.com/archive.tar> /archive-content
    ```
    
5. **ENV**:
    - This instruction is used to set environment variables that will be available in your container.
    <br>
    
    ```docker
    ENV PATH $value
    ```
    
6. **ENTRYPOINT and CMD**:
     - `ENTRYPOINT` sets the processes to run when a container starts. It is not modifiable by the user.
     - `CMD` provides default arguments to that process, changeable and modifiable by users.
    <br>
    
    ```docker
    ENTRYPOINT ["python"]       # Set the entrypoint to the Python interpreter
    CMD ["python", "main.py"]
    ```
    
7. **EXPOSE**:
     - Expose a port from the container.
       
    <br>
    
    ```docker
    EXPOSE 8080
    ```
    
8. **WORKDIR**:
     - Sets the working directory for all following commands. Similar to `cd` in Linux.
    <br>
    
    ```docker
    WORKDIR /app
    ```
    
    ---
    
**Diff between CMD and Entrypoint :**
    
  - Entrypoint is an instruction where you can define what has to run when the container is initiated. I mean after starting
  - CMD is you can attach additional commands to run after the running of Entrypoint instructions completion.
    
  ➜  [Docker Best Practices: Choosing Between RUN, CMD, and ENTRYPOINT | Docker](https://www.docker.com/blog/docker-best-practices-choosing-between-run-cmd-and-entrypoint/)

---

**Difference Between Docker Registry and Repository :**
    
#### 📌 Docker Registry :
    
  - Definition: Stores Docker images.
  - Functionality: Centralized location for image storage and distribution.
  - Examples: Docker Hub, Google Container Registry.
  - Usage: Users push and pull images.
    
**Docker Repository :**
    
  - **Definition**: Collection of related Docker images with the same name but different tags.
  - **Functionality**: Organizes and manages versions of Docker images.
  - **Examples**: Contains images for different versions of an application.
  - **Usage**: Users pull specific versions of images using tags.
 
    
### Buildah Tool:
    
![image](https://github.com/user-attachments/assets/b6736041-8609-412d-99f4-1388a2c726d2)
    
Buildah is a command-line tool used for building Open Container Initiative (OCI) and Docker-compatible container images. It provides a flexible and efficient way to create container images without requiring a running Docker daemon.
    
**Key Features :**
    
  - **Daemonless**: Buildah operates without needing a running container daemon, making it lightweight and secure.
  - **Scripting**: Allows for complex scripting and automation of image building.
  - **Compatibility**: Supports OCI and Docker image formats.
  - **Rootless Mode**: Can be run as a non-root user, enhancing security.
    
**Advantages :**

    
   - **Efficiency**: Lightweight and fast due to the absence of a daemon.
   - **Security**: Increased security with rootless mode and no need for a root daemon.
   - **Flexibility**: Fine-grained control over the build process, supporting scripting and custom workflows.

--- 

**Docker Port Mapping/Port Binding :**

  - **Definition**: Port mapping (or port binding) connects ports on a Docker container to ports on the host machine.
  - **Purpose**: Allows access to container services from outside the container.
  - **Syntax**: `-p hostPort:containerPort`
  - **Example**: `docker run -p 8080:80 myapp` maps port 8080 on the host to port 80 in the container.

    --- 
    
**Docker volumes:**
    
**Docker Volume**: A Docker volume is a persistent data storage mechanism used to manage data in Docker containers. Volumes enable data to persist even when containers are removed, allowing for data sharing among containers and better data management.
    
    Create and Use a Volume
    
    - **Run a container with a volume:**
    
    ```bash
    $ docker run -v /opt/datadir:/var/lib/mysql <containername>
    ```
    
    **Docker Storage**
    
    - Docker uses storage drivers from the OS. By default, all Docker data is stored under:
    
    ```bash
    /var/lib/docker > Volumes > data-volume
    ```
    
    **Create a persistent volume:**
    
    ```bash
    $ docker volume create data-volume
    ```
    
    **Attach a Volume (Mounting)**
    
    - **Run a container and attach a volume:**
    
    ```bash
    $ docker run -v data-volume:/var/lib/mysql <containername>
    
    *(If the `data-volume` is not created, it will be created at runtime)*
    ```
    
    **Bind Mount**
    
    - **Using a bind mount:**
    
    ```
    $ docker run -v /data/mysql:/var/lib/mysql mysql
    ```
    
    **New Way to Use Bind Mount**
    
    - **Run a container with a bind mount using the `-mount` flag:**
    
    ```bash
    $ docker run \
      --mount type=bind,source=/data/mysql,target=/var/lib/mysql \
      mysql
    ```
    
- **Docker Networking:**
    
    **Docker networking** allows containers to communicate with each other and with the host system. There are several network drivers available in Docker:
    
    - **Bridge**: The default network driver for standalone containers.
    - **Host**: Removes network isolation between the container and the Docker host.
    - **Overlay**: Enables communication between multiple Docker daemons.
    - **Macvlan**: Assigns a MAC address to a container, making it appear as a physical device on the network.
    - **None**: Disables all networking for the container.
    
     **Bridge Network**
    
    ---
    
    - **Definition**: The default network driver. Containers on the same bridge network can communicate with each other.
    - **Commands**:
        - **Create a Bridge Network**:
            
            ```bash
            $ docker network create --driver bridge my_bridge
            ```
            
        - **Run a Container on a Bridge Network**
            
            ```bash
            $ docker run --network my_bridge --name container1 nginx
            ```
            
        - **List Networks**:
            
            ```bash
            $ docker network ls
            ```
            
        - **Inspect a Network**:
            
            ```bash
            $ docker network inspect my_bridge
            ```
            
        - **Connect a Running Container to a Network**:
            
            ```bash
            $ docker network connect my_bridge container1
            ```
            
        - **Disconnect a Running Container from a Network**:
            
            ```bash
            $ docker network disconnect my_bridge container1
            ```
            
    
     ****
    
    **Host Network**
    
    ---
    
    - **Definition**: The container shares the host’s network stack.
    - **Commands**:
        - **Run a Container with Host Network**:
            
            ```bash
            $ docker run --network host --name my_container nginx
            ```
            
    
     ****
    
    **Overlay Network**
    
    ---
    
    - **Definition**: Enables swarm services to communicate with each other.
    - **Commands**:
        - **Create an Overlay Network**:
            
            ```bash
            $ docker network create --driver overlay my_overlay
            ```
            
        - **Run a Service on an Overlay Network**:
            
            ```bash
            $ docker service create --name my_service --network my_overlay nginx
            ```
            
    
     **Macvlan Network**
    
    ---
    
    - **Definition**: Assigns a MAC address to the container, making it appear as a physical device on the network.
    - **Commands**:
        - **Create a Macvlan Network**:
            
            ```bash
            $ docker network create -d macvlan \\
              --subnet=192.168.1.0/24 \\
              --gateway=192.168.1.1 \\
              -o parent=eth0 my_macvlan
            ```
            
        - **Run a Container on a Macvlan Network**:
            
            ```bash
            $ docker run --network my_macvlan --name my_container nginx
            ```
            
    
     
    
     **None Network**
    
    ---
    
    - **Definition**: Disables all networking for the container.
    - **Commands**:
        - **Run a Container with No Network**:
            
            ```bash
            $ docker run --network none --name my_container nginx
            ```
            
    
    ### General Networking Commands
    
    - **Remove a Network**:
        
        ```bash
        $ docker network rm my_network
        ```
        
    - **Prune Unused Networks**:
        
        ```bash
        $ docker network prune
        ```
        
    
    ---
    
- **Docker compose :**
    
    **Docker Compose** is a tool for defining and running multi-container Docker applications. It uses a YAML file to configure the application’s services, networks, and volumes.
    
    **Docker Compose Examples :**
    
    https://github.com/docker/awesome-compose
    
    **Basic Commands**
    
    - **Start services defined in a `docker-compose.yml`**:
        
        ```bash
        $ docker-compose up
        ```
        
    - **Start services in detached mode**:
        
        ```bash
        $ docker-compose up -d
        ```
        
    - **Stop services**:
        
        ```bash
        $ docker-compose down
        ```
        
    - **Restart services**:
        
        ```bash
        $ docker-compose restart
        ```
        
    - **View service logs**:
        
        ```bash
        $ docker-compose logs
        ```
        
    - **Build or rebuild services**:
        
        ```bash
        $ docker-compose build
        ```
        
    - **List all running services**:
        
        ```bash
        $ docker-compose  ps
        ```
        
    
    ### Docker Compose File Structure
    
    ---
    
    - **`version`**: Specify the Compose file format version.
    - **`services`**: Define individual services (containers).
    - **`networks`**: Define custom networks.
    - **`volumes`**: Define persistent storage volumes.
    
    ### Example `docker-compose.yml`
    
    ```yaml
    version: '3.8'
    
    services:
      web:
        image: nginx
        ports:
          - "8080:80"
        volumes:
          - ./web:/usr/share/nginx/html
        networks:
          - webnet
    
      app:
        image: myapp
        environment:
          - APP_ENV=production
        networks:
          - webnet
    
    networks:
      webnet:
    
    volumes:
      data-volume:
    ```
    
    ### Key Docker Compose Commands
    
    ---
    
    - **Start a single service**:
        
        ```bash
        $ docker-compose up <service_name>
        ```
        
    - **Stop a single service**:
        
        ```bash
        $ docker-compose stop <service_name>
        ```
        
    - **Remove a single service's container**:
        
        ```bash
        $ docker-compose rm <service_name>
        ```
        
    - **Scale services**:
        
        ```bash
        $ docker-compose up --scale <service_name>=<number>
        ```
        
    
    ### Environment Variables
    
    ---
    
    - **Using `.env` file**:
        - Create a `.env` file:
            
            ```
            APP_ENV=production
            DATABASE_URL=mysql://user:pass@db:3306/mydatabase
            ```
            
        - Reference in `docker-compose.yml`:
            
            ```yaml
            version: '3.8'
            
            services:
              app:
                image: myapp
                environment:
                  - APP_ENV=${APP_ENV}
                  - DATABASE_URL=${DATABASE_URL}
            ```
            
    
    ### Networking
    
    ---
    
    - **Default Network**: Compose automatically creates a default network for your services.
    - **Custom Networks**:
        
        ```yaml
        networks:
          webnet:
            driver: bridge
        ```
        
    
    ### Volumes
    
    ---
    
    - **Named Volumes**:
        
        ```yaml
        volumes:
          data-volume:
        ```
        
    - **Mounting Volumes**:
        
        ```yaml
        services:
          db:
            image: mysql
            volumes:
              - data-volume:/var/lib/mysql
        ```
        
    
    ### Common Use Cases
    
    ---
    
    - **Running Tests**:
        
        ```
        $ docker-compose run <service_name> <test_command>
        ```
        
    - **One-off Commands**:
        
        ```
        $ docker-compose run <service_name> <command>
        ```
        
    
    ---
