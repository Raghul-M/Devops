
## Introduction:

![image](https://github.com/user-attachments/assets/60f5c658-234b-4663-98f9-ff644ed1893a)


**Kubernetes** is a container orchestration platform. Containers are ephemeral, meaning they have a short life span and will work until the process is running, crashes (die & revive), or runs out of resource allocation.

- Open source and portable platform
- Automates scaling of workloads
- Groups containers into logical units
- Donated by Google to CNCF
- Written in Go programming language
- Container orchestration tool

**Problems in Docker:**


- **Single host failure**
- **Manual healing** (If it is killed) -> **Auto healing** (Kubernetes)
- **Doesn't scale** -> **Auto scaling** (Kubernetes)
- **Simple platform lacks enterprise-level features**: load balancer, firewall, autoscale, API gateway, healing

**Solutions for the above problems:**
- **Cluster**: A group of nodes (Master nodes & worker nodes). When one cluster doesn’t get the resource, it puts it in another node.
- **Replica set/Replication controller**: Auto scaling
- **Auto healing**: Achieved using API server
- **Enterprise-level container orchestration platform**: Load balancing, advanced networking, security

---

## KUBERNETES ARCHITECTURE:

![image](https://github.com/user-attachments/assets/218c119d-6169-478e-9e65-59272b2da522)

Kubernetes architecture consists of **Master** and **Worker nodes.** Worker nodes contain `kubelet`. `Kubelet` is an agent that runs on each node in the cluster and manages pods, the smallest deployment units where containers are deployed.

### Master node components:

1. **API Server**: The front end for the Kubernetes control plane, passing information from the master to the worker node via:
    - UI
    - CLI
    - API
2. **Controller Manager**: Keeps track of what is happening in the Kubernetes cluster. It includes:
    - Node controller
    - Replication controller
    - Endpoints Controller
    - Service Account & Token Controller
3. **Scheduler**: Manages Pods Placement
4. **Cloud Control Manager**
5. **etcd**: Key-value store for cluster data

### Control Plane (Master node)


Runtime describes software/instructions executed while your program is running, especially those you did not write explicitly but are necessary for proper code execution.

- A **container runtime** is a program that allows a container to start and run on a machine.
- A **Pod** in Kubernetes is similar to a container in Docker, which is the **smallest deployable part**.
- In Docker, everything is managed by Docker Engine.

### Components of Data Plane (Worker node):

1. **kubelet**
2. **Container runtime**
3. **kube-proxy**
4. **kubelet**: Responsible for handling the creation, checking status, and health of pods in worker nodes. These instructions are sent by the master node (control plane), ensuring the pod is running and sending the status.
5. **Container runtime**: Mandatory in Kubernetes. You can use `crio`, `containerd`, `Docker`, etc., which meet Kubernetes standards.
6. **kube-proxy**: Similar to Docker bridge, used for networking between the containers. In Kubernetes, it is responsible for allocating IP addresses, load balancing, using IP tables for networking, etc.

---

## MINIKUBE FOR LEARNING KUBERNETES:

**To download Minikube:**

- Install Minikube
- Install kubectl

**Minikube**: It is a local Kubernetes, focusing on making it easy to learn and develop for Kubernetes.

**kind**: Lets you run Kubernetes on your local computer. This tool requires Docker or Podman to install.

**Difference between Minikube and kubectl:**

kubectl is like the remote control for managing any Kubernetes cluster, while Minikube is a mini version of Kubernetes that you can run on your own computer for local development and testing.

---

### Pod:

![image](https://github.com/user-attachments/assets/317714c6-af2c-447c-bcb3-b2dbd8fb024c)


- A definition of how to run a container. It is similar to arguments we pass to run the container but in Kubernetes it is in `podspec.yaml` file, known as a YAML manifest.
- A Pod can contain single or multiple containers. Multiple containers in a Pod share network and storage. The Pod gets a cluster IP to access the application inside the container; you don't get an IP for the container inside the Pod.
- A Pod is a wrapper for containers. In production, you can read the `pod.yaml` file to understand thousands of containers.

### Kubectl:

![image](https://github.com/user-attachments/assets/a8fade19-bd6c-481e-947d-147f545cb884)


It is a CLI for Kubernetes cluster.

**Examples:**

- `kubectl get nodes`
- `minikube start` (creates a cluster, under the hood it creates a VM -> single node Kubernetes cluster)
- `kubectl create -f pod.yaml` (creates a Pod)
- `kubectl get pods` (lists all running Pods, similar to `docker ps`)
- `kubectl get pods -o wide` (provides complete details of the Pod like IP, etc.)
- `minikube ssh` (used to login to the cluster)
- `kubectl delete pod nginx` (deletes a Pod)

----

### Deployments:

![image](https://github.com/user-attachments/assets/8e0767f1-243d-4761-ba34-44ac87e7b709)


- A wrapper for Pod to enable Auto healing and Auto scaling.
- `kubectl describe pod <podname>` (returns the status of everything from the Pod)
- `kubectl logs <podname>` (shows if there are any issue logs in the Pod, useful for troubleshooting)

<aside>
  
📌 **Note:**

To debug the Pod or the application, use these commands to clear the issue:

1. `kubectl describe pod <podname>`
2. `kubectl logs <podname>`
   
</aside>

**ReplicaSet**: A Kubernetes controller responsible for auto healing.

**Deployment**: Contains the desired state and the ReplicaSet ensures and changes based on the desired state to actual state.

**Examples:**

- `kubectl get deploy`
- `kubectl get rs` (rs - ReplicaSet)
- `kubectl apply -f deployment.yml`
- `kubectl get pods -w` (watches the Pods)

> If you delete a Pod, ReplicaSet will create another Pod simultaneously while terminating.


### Difference between Container vs Pod vs Deployment:

- **Container**: Pass arguments in the command line to run it.
- **Pod**: Specify everything in the `pod.yaml` file.
- **Deployment**: Enables auto healing and auto scaling. Kubernetes suggests deploying the application as a deployment instead of a plain Pod. In deployment, it also creates Pods (Deployment resource -> ReplicaSet -> Pod).

---

## Kubernetes Services:

![image](https://github.com/user-attachments/assets/7a4454ca-6845-4116-91bb-e822b79a6c8e)


### Advantages:

1. Load balancing
2. Service discovery
3. Expose to the external world

**svc - service**

- Performs load balancing using `kube-proxy`. Service is applied on top of deployment for load balancing because if we directly give the IP address, if it is deleted and auto-healed, the IP changes and the application is not accessible. For this reason, we use service to take care of it.
- Uses Labels & selectors to keep track and perform discovery. Labels are applied to the Pod. Because we are using label, the ReplicaSet and service look into the label of the Pod for load balancing instead of IP address.
- Service exposes the application outside the Kubernetes cluster.

**Example:**

```yaml
label:
  app: payment
```

### Three types of services:

1. **Cluster IP**: Default (inside the Kubernetes cluster)
2. **NodePort**: Allows access inside your org or network (worker node IP or EC2)
3. **LoadBalancer**: Exposes application to the outside world (by default not available in Minikube, available in cloud providers)

---

## Interview Questions:

1. Difference between Docker and Kubernetes:
2. Main components of Kubernetes architecture: [ **Control plane** and **data plane** ]
3. Difference between Docker Swarm and Kubernetes:
- **Docker Swarm:** Small applications, doesn’t have enterprise-level support
- **Kubernetes:** Large and mid-level applications with enterprise standard solutions
4. Difference between Container and Pod:
- A **Pod** in Kubernetes is a runtime specification of a container in Docker. A Pod provides a more declarative way of defining using YAML, and you can run more than one container in a Pod. Pod is the smallest unit in Kubernetes.
5. Namespaces in Kubernetes:
- In Kubernetes, a **namespace** is a logical isolation of resources, network, RBAC, etc. For example, if there are two projects using the same Kubernetes cluster, one project can use ns1 and another can use ns2 without any overlap and authentication problems.
6. Role of kube-proxy:
- **kube-proxy** works by maintaining a set of network rules on each node in a cluster, which are updated dynamically as services are added or removed. When a client sends a request to a service, kube-proxy intercepts the request, looks up the destination endpoint for the service, and routes the request accordingly.
7. Different types of services within Kubernetes:
- **Three types:** Cluster IP mode, NodePort mode, and LoadBalancer mode.
8. Difference between NodePort mode and LoadBalancer mode:
- **NodePort**: kube-proxy updates the IP tables with node IP address and port chosen in the service configuration to access the Pods.
- **LoadBalancer**: The Cloud Control Manager (CCM) creates an external load balancer IP using the underlying cloud provider logic in the CCM. Users can access services using the external IP.
9. Role of kubelet:
- **kubelet** manages the containers scheduled to run on that node. It ensures that containers are running and healthy, and that the resources they need are available.
10. Difference between Pod and Node:
- A Pod is a group of containers that manage shared resources and run application instances, while a Node is a physical or virtual server that hosts Pods and runs containerized applications.
11. Day-to-day activities in Kubernetes or DevOps?

---

### Detailed Overview of Kubernetes Concepts and Best Practices

### **Using kubectl Verbose Mode**

To see detailed API calls made by `kubectl`, you can use the `-v` flag with a verbosity level of 9:

```bash
$ kubectl get svc -v=9
```

<aside>
  
📌 **Note:**

`kubectl get svs -v=9` (Verbose mode, gives the detailed API call for kubectl via API. 9 )

</aside>

This command provides in-depth details of the API interactions behind `kubectl` commands.

### **Minikube and Kubernetes Services**


1. **Retrieve Minikube IP:**
    
    ```bash
    $ minikube ip
    ```
    
    This command retrieves the IP address of the Minikube cluster.
    
2. **Editing a Service:**
    
    ```bash
    $ kubectl edit svc <service-name>
    ```
    
    Edit the service definition to change properties, such as the service type.
    
3. **Changing Service Type:**
Update the service type in the YAML file (e.g., from `ClusterIP` to `LoadBalancer`):
    
    ```yaml
    spec:
      type: LoadBalancer
    ```
    
    Apply changes by saving the file.
    

---

### **Ingress in Kubernetes**
![image](https://github.com/user-attachments/assets/0051ffdb-7b41-4feb-bb95-30f220fecea1)


### **Capabilities:**

- Supports advanced load balancing features:
    - Ratio-based
    - Sticky sessions
    - Path-based
    - Domain-based
    - Whitelisting/Blacklisting

### **Comparison with LoadBalancer Service:**


- **Ingress:**
    - Collection of rules managing external access to services within a cluster.
    - Acts as a single entry point for multiple services.
- **Service Type LoadBalancer:**
    - Exposes a single service to the outside world.
---

### **Ingress Controller:**

- An Ingress Controller, like NGINX or HA Proxy, manages the Ingress resources and routes external traffic to the correct services.
- Installation Example:
    
    ```bash
    $ kubectl apply -f <https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml>
    ```
    
- After installation, create and apply Ingress resources:
    
    ```bash
    $ kubectl apply -f ingress.yml
    $ kubectl get ingress
    ```
---

### **ConfigMaps and Secrets**

#### **ConfigMaps:**

- Store non-sensitive configuration data.
- Example usage in a Pod:
    
    ```yaml
    containers:
    - name: app
      image: python:3
      env:
        - name: DB_PORT
          valueFrom:
            configMapKeyRef:
              name: test-cm
              key: db-port
    
    ```
    

#### **Secrets:**

- Store sensitive data like passwords and API keys.
- Example usage in a Pod:
    
    ```yaml
    containers:
    - name: app
      image: python:3
      env:
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: password
    
    ```
 ---   

#### **Volume Mounts:**

- ConfigMaps and Secrets can be mounted as files for applications that need to read them.
- Example for ConfigMap:
    
    ```yaml
    spec:
      containers:
        - name: app
          image: busybox:1.28
          command: ['sh', '-c', 'echo "This is running!" && tail -f /dev/null']
          volumeMounts:
            - name: config-vol
              mountPath: /etc/config
      volumes:
        - name: config-vol
          configMap:
            name: log-config
            items:
              - key: log_level
                path: log_level
    
    ```
---

### **RBAC (Role-Based Access Control)**


#### **Components:**

1. **Roles and ClusterRoles:**
    - Define permissions on resources.
2. **RoleBindings and ClusterRoleBindings:**
    - Bind roles to users, groups, or service accounts.

#### **User and Service Account Management:**

- Users are managed by external identity providers (e.g., Google, LDAP, AWS IAM).
- Service accounts are used within clusters for assigning permissions to Pods.

#### **Example Role and RoleBinding:**

**Role:**
    
```yaml
    kind: Role
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      namespace: default
      name: pod-reader
    rules:
    - apiGroups: [""]
      resources: ["pods"]
      verbs: ["get", "watch", "list"]
```
    
**Role Binding:**
    
```yaml
    kind: RoleBinding
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      name: read-pods
      namespace: default
    subjects:
    - kind: User
      name: "janedoe"
      apiGroup: rbac.authorization.k8s.io
    roleRef:
      kind: Role
      name: pod-reader
      apiGroup: rbac.authorization.k8s.io
```
---

### **Monitoring with Prometheus and Grafana**

![image](https://github.com/user-attachments/assets/6a797ec5-be78-4625-b541-48fac20c1741)


- **Prometheus:**
    - Collects metrics from various sources.
- **Grafana:**
    - Visualizes time-series data from Prometheus.

---

### **Helm**

- **Helm:**
    - A package manager for Kubernetes.
    - Uses Helm charts to define, install, and manage Kubernetes applications.
- **Installation Example:**
    
    ```bash
    $ helm repo add stable <https://charts.helm.sh/stable>
    $ helm install my-release stable/grafana
    ```    
---

### **Custom Resource Definitions (CRDs)**

![image](https://github.com/user-attachments/assets/062fabf8-4028-4e93-afd7-e791c1f6a434)



### **CRDs:**

- Extend Kubernetes API with custom resources.
- Custom controllers manage the lifecycle of these custom resources.
- Example definition:
    
    ```yaml
    apiVersion: apiextensions.k8s.io/v1
    kind: CustomResourceDefinition
    metadata:
      name: myresources.mydomain.com
    spec:
      group: mydomain.com
      versions:
        - name: v1
          served: true
          storage: true
      scope: Namespaced
      names:
        plural: myresources
        singular: myresource
        kind: MyResource
        shortNames:
        - myres
    ```
    
- Custom controllers can be implemented using **Golang** with the `controller-runtime` library.
