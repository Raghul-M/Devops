## AWS Production-Level Network Infrastructure : VPC with servers in private subnets and NAT

<div align="center">
  <img src="https://github.com/user-attachments/assets/ce48695b-fb94-4e35-834f-b9e361b48569" alt="vpc-example-private-subnets">
</div>

<br>

This example demonstrates how to create a **VPC** for servers in a **production environment**.  

To improve **resiliency**, you deploy the servers across **two Availability Zones** using an **Auto Scaling group** and an **Application Load Balancer**. For additional security, the servers are deployed in **private subnets**. The servers receive requests through the **load balancer** and can connect to the internet via a **NAT gateway**. To enhance resiliency, the NAT gateway is deployed in both Availability Zones.

## Architecture Overview

- The **VPC** includes **public subnets** and **private subnets** in **two Availability Zones**.
- Each **public subnet** contains a **NAT gateway** and a **load balancer node**.
- The servers:
  - Run in **private subnets**.
  - Are launched and terminated by an **Auto Scaling group**.
  - Receive traffic from the **load balancer**.
  - Connect to the internet through the **NAT gateway**.

Key components:
- **Auto Scaling Group**  
- **Load Balancer**  
- **Target Group**  
- **Bastion Host**

---

## Step 1: Create a Custom VPC

![Screenshot from 2024-11-22 20-00-09](https://github.com/user-attachments/assets/b3a2c9be-065d-4e2e-b3be-375782b61aa7)

1. Go to **VPC** and select **Create VPC**.
2. Set the **IP address range** and create:
   - **2 Public Subnets**
   - **2 Private Subnets**  
3. Name the VPC as `aws-prod`.
   
<div align="center">
  <img src="https://github.com/user-attachments/assets/eee3bb98-e57b-4bec-8571-48c5ca27e983" alt="vpc-example-private-subnets">
</div>


4. For each Availability Zone (AZ), select the option to deploy **1 subnet per AZ**.
5. Click **Create VPC** and wait for the process to complete.

---


## Step 2: Create an Auto Scaling Group

![Screenshot from 2024-11-22 20-38-13](https://github.com/user-attachments/assets/d6511b09-85b3-4846-a586-af983fc9b02e)


1. Go to **EC2 > Auto Scaling Groups** and click **Create Auto Scaling Group**.
2. Name it as `aws-prod` (or any preferred name).
3. Create a launch template:
   - Name the template and select an **Amazon Machine Image (AMI)** (e.g., Ubuntu).
   - Create a key pair for **authentication** purposes.
   - Configure a **new security group**:
     - Add **inbound rules** as shown in the corresponding image.
       
<br>

![Screenshot from 2024-11-22 20-12-50](https://github.com/user-attachments/assets/2f400d60-6f89-433c-b43b-f0509e7fe4fc)

<br>

   - Click **Create Launch Template**.
4. Create an Auto Scaling Group:
   - Use the launch template created earlier.
   - Select the **VPC** and **both private subnets**.
   - Set the **Group Size and Scaling Options** as shown in the image.
     
<br> 

![Screenshot from 2024-11-22 20-17-31](https://github.com/user-attachments/assets/7b5a8309-9f23-4b82-b3c6-ded6515e5ed9) 

<br>

![Screenshot from 2024-11-22 20-17-22](https://github.com/user-attachments/assets/c6414dbf-2845-4190-ae56-969923263c6a)

<br>

5. Once created, it will launch **2 instances** (one in `us-east-1a` and one in `us-east-1b`).
   
<br>     

![Screenshot from 2024-11-22 20-52-01](https://github.com/user-attachments/assets/bdc2fa9f-460b-4831-b6f5-9d1c2de1124b)

---

## Step 3: Create a Bastion Host

To ensure private subnet IPs do not leak to the internet, create a **bastion host** in the same VPC.

1. Launch a bastion host instance:
   - Use the **network settings** configuration from the image provided.
<br>

![Screenshot from 2024-11-22 20-54-20](https://github.com/user-attachments/assets/774251e0-1ae9-4d5e-ad51-de6eaebfbaf2)

<br>   

2. SSH into the bastion host from your system using the key pair:
   ```bash
   ssh -i <key.pem> ubuntu@<bastion-host-public-ip>
   ```
3. Copy the key pair to the bastion host instance:
   ```bash
   scp -i <key.pem> <key.pem> ubuntu@<bastion-host-ip>:/home/ubuntu
   ```
   If you encounter a **permission denied** error, use:
   ```bash
   chmod 400 ./aws-login.pem
   ```
4. Verify the key file in the bastion host by running:
   ```bash
   ssh -i <key.pem> ubuntu@<bastion-host-public-ip>
   ls
   ```

---

## Step 4: Log in to the Auto Scaling Instances

1. From the bastion host, SSH into one of the instances created by the Auto Scaling Group:
   - Copy the **private IP address** of the instance.
   - Run the following command from the bastion host:
     ```bash
     ssh -i <key.pem> ubuntu@<private-ip>
     ```
2. Once logged in:
   - Check if **Python 3** is installed.
   - Create a simple HTML page:
     ```bash
     vim index.html
     ```
     Content:
     ```html
     <!DOCTYPE html>
     <html>
     <head>
     <title>Page Title</title>
     </head>
     <body>
     <h1>This is Application-1</h1>
     </body>
     </html>
     ```
   - Run a Python HTTP server:
     ```bash
     python3 -m http.server 8000
     ```

3. Repeat the steps for the second instance, but modify the HTML:
   ```html
   <h1>This is Application-2 for Load Balancing</h1>
   ```

---

## Step 5: Create a Load Balancer

1. Go to **EC2 > Load Balancers** and create an **Application Load Balancer**.
   - Choose **Internet-Facing**, **IPv4**, and select the **VPC** created earlier.
   - Select **both public subnets** from the Availability Zones.
2. Create a **Target Group**:
   - Use **HTTP** on port **8000**.
   - Add the Auto Scaling Group instances to the target group.
3. Attach the target group to the load balancer and complete the creation process.

---

## Step 6: Final Steps

1. Wait for the load balancer to complete provisioning.
2. Update the **security group** to allow **HTTP traffic on port 80**.
3. Copy the **DNS name** of the load balancer and test it in a browser.

## Output :

![Screenshot from 2024-11-22 21-35-01](https://github.com/user-attachments/assets/8ae4a2d0-f00b-4a87-82ea-8017d10c0484)

![Screenshot from 2024-11-22 21-35-10](https://github.com/user-attachments/assets/0f5bb121-91df-4e56-8079-3407a3f73454)

