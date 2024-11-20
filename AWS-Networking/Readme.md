## AWS Networking

![hero](https://github.com/user-attachments/assets/a5fb49ac-b2db-4391-a7fd-de5e5ef0388e)

### **VPC - Virtual Private Cloud**

Initially, around 2013–2014, AWS created EC2 instances for different companies on the same server. This posed a security risk—if one company's EC2 instance was hacked, the hacker could potentially gain access to other companies’ instances on the same server.

To address this issue, AWS introduced the **VPC (Virtual Private Cloud)**. A VPC is a company-specific, isolated network within AWS. The size of a VPC is defined by the IP address range set by a DevOps engineer or AWS cloud engineer.
   
   ---
### **Key Components of a VPC**

![AWS-Nacl-vs-Security-group](https://github.com/user-attachments/assets/684cd68d-7732-4bf6-8eca-3abf8836ace0)

### **Gateway**

- The gateway acts as the entry point into the VPC.
- A **public subnet** connects to the internet via the **Internet Gateway (IGW)**.
- Requests are routed to a **load balancer**, which directs traffic to the application hosted in a **private subnet**.
- The path between the application (in the private subnet) and the load balancer is defined using **route tables** or **routers**.

### **Security Group (SG)**

Before reaching the application, traffic passes through the **Security Group** (SG), which:

- Ensures only authorized requests are allowed, based on IP and port configurations.

### **NAT Gateway**

- A **NAT Gateway** (Network Address Translation Gateway) allows resources in the private subnet to access the internet for outgoing requests while keeping them inaccessible from the outside.

#### **📌 Security in AWS**

AWS security operates on a **shared responsibility model**:

- AWS handles security **of the cloud** (e.g., physical servers and infrastructure).
- The customer is responsible for security **in the cloud** (e.g., configurations, access control).
---

![0_px7fcWcXMnmCkNC3](https://github.com/user-attachments/assets/21d0d726-ccbf-496b-acdf-c69a8796d241)


### **Security Group**
    
**Security Group (Instance Level)**    

 - Security Groups operate at the **instance level**.
 - By default, AWS does not allow any incoming traffic; users must configure rules to allow specific ports (e.g., port 8080).
    
- Consists of:
     - **Inbound traffic**: Incoming requests to the instance.
     - **Outbound traffic**: Outgoing requests made by the application (e.g., accessing other webpages).
    
**Default Behavior:** 
    
  - **Inbound Traffic**: Denied by default in the default security group.
  - **Outbound Traffic**: Allowed by default, except for **port 25** (used for mailing services).
    
    
**📌 Why block port 25?**
    
    AWS restricts port 25 to prevent IP exposure, spam activities, and misuse for mailing services.
 ---
    
### **NACL**
    
**NACL - Network Access Control List (Subnet Level)**
    
- NACLs operate at the **subnet level**, providing another layer of security.
- **Primary Use Cases**:
  - Deny specific IPs or ports, even if they are allowed in the SG.
  - Apply consistent rules across all EC2 instances in a subnet, reducing the need to configure rules on each instance.
    
- NACLs are often used by admins or DevOps engineers to override less restrictive rules set by developers in Security Groups.
  
- Rules in NACLs are evaluated **based on rule numbers**.
  - Lower rule numbers (e.g., 100) are applied **first**, followed by higher numbers (e.g., 200).
  - This allows precise control over the order of rule evaluation.
  
- NACLs allow both **allow** and **deny** rules, unlike Security Groups, which only allow **allow** rules.
    
**Primary Use Cases**:
    
  1. **Deny Specific IPs or Ports**: NACLs can block traffic from certain IPs or ports, even if Security Groups allow it.
  2. **Apply Consistent Rules**: Instead of configuring rules for each EC2 instance, NACLs apply rules automatically to all instances in a subnet.
    
**Example**:
    
  - **Rule 100:** Allow traffic from IP range 192.168.0.0/16.
  - **Rule 200:** Deny traffic from IP 192.168.0.5.
    - In this case, traffic from 192.168.0.5 will be blocked, as the deny rule (200) is evaluated after the allow rule (100).
    
By leveraging NACL rule numbering, administrators can prioritize and fine-tune traffic control efficiently.
    
By using a combination of **Security Groups** and **NACLs**, AWS provides a robust and flexible framework for managing traffic to and from your applications.
