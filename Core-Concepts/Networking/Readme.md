# Networking

![image (6)](https://github.com/user-attachments/assets/07210b84-cb56-4f6e-94b3-1e6da7ade440)

Networking refers to the practice of connecting computers and other devices to share resources (like files, internet access, or applications) and communicate with each other. Networking can be as simple as connecting two computers at home or as complex as connecting millions of devices globally, as seen with the internet.

### Types of Networks


- **LAN (Local Area Network):** A network within a small geographic area (e.g., home, office).
- **WAN (Wide Area Network):** A network that spans a large geographic area (e.g., the internet).
- **MAN (Metropolitan Area Network):** A network that covers a city or large campus.



### 📌  Networking Devices

- Router: For directing traffic between networks.
- Switch: For connecting devices within the same network.
- Hub: A basic device for connecting multiple devices in a network.
- Modem: Converts signals for internet access.
- Firewall: A security device that monitors and controls incoming and outgoing network traffic.

---

#### IP Address (Internet Protocol Address)



An IP address is a unique identifier assigned to each device connected to a network. This address allows devices to locate and communicate with each other.

**Types of IP Addresses:**

1. IPv4 (Internet Protocol Version 4)
2. IPv6 (Internet Protocol Version 6)

**IPv4**


- IPv4 is the standard for generating unique identification numbers for devices in a network. It’s currently the most widely used protocol, represented in a format like `10.1.2.3`

**Structure of an IPv4 Address**

- IPv4 addresses consist of four sets of numbers (called "octets"), separated by periods.
- Each number in an IPv4 address can range from 0 to 255, meaning each octet is 8 bits long, as a byte in computing is equivalent to 8 bits.
    
    `Example: 192.168.0.1`
    <br>
- **Why Does Each Part Range from 0 to 255?** 
    
    Each octet in an IPv4 address is one byte, or 8 bits. Because each bit can be either 0 or 1, there are `2^7` possible values for each octet, ranging from 0 to 255. This results in a total of approximately 4.3 billion possible IPv4 addresses (specifically, 2^32, since there are four octets, each with 8 bits). 
    - IP Address Length: An IPv4 address has a total of 32 bits `(4 bytes x 8 bits = 32 bits)`.
    - Octet: Since each octet is a byte (8 bits), it’s also known as an "octet" format.
        - Binary Range: Each octet's maximum value (255) is based on binary representation, where the highest binary value with 8 bits is 11111111, equating to 255 in decimal.

- **Why Not a Larger Range `(e.g., 0-1000)` ?**
    
    The 0-255 range is a limitation of the 8-bit structure of each octet in an IPv4 address. Since the standard defines an IP address as 32 bits long (with each segment limited to 8 bits), the 0-255 range is fixed. Increasing the range would mean changing the underlying protocol, which would disrupt compatibility and require a global overhaul.
    

**IPv6**


To address the limitations of IPv4, IPv6 was introduced, which uses 128 bits for each address (instead of 32 bits), allowing for vastly more unique addresses. This expansion supports the growing number of devices and demand for IP addresses in the modern world.

**Example IPv6 Address:** `2001:0db8:85a3:0000:0000:8a2e:0370:7334`

---

### Subnet

Subnet is the process of dividing a larger network into smaller, manageable sub-networks (subnets). This is done for several reasons:

- **Security:** Isolating certain parts of a network for additional security (e.g., keeping sensitive data in a separate subnet).
- **Access Control:** Limiting access to one domain or set of users, ensuring they can only access resources in their designated subnet.
- **Network Efficiency:** Reducing network congestion and improving overall performance by controlling broadcast traffic.

#### Advantages of Subnetting

- **Security:** Helps segment the network into isolated parts, allowing for more control over traffic and improved security policies.
- **Privacy:** Sensitive or private information can be restricted to a specific subnet.
- **Isolation:** Prevents unauthorized access between subnets, as they need routing to communicate with each other.

#### Types of Subnets

1. **Private Subnet:**
    - No direct access to the internet. Used for resources like databases, internal servers, or other services that don’t need to be exposed to the internet.
2. **Public Subnet:**
    - Has access to the internet. Devices in this subnet can communicate with external services via an internet gateway. Public subnets are typically used for services like web servers, load balancers, or any other services that need to be externally accessible.

```
📌 How do Public Subnets Access the Internet?

 - Public subnets access the internet by routing traffic through an Internet Gateway.
   This allows devices in the public subnet to communicate with external networks.
```

### Subnetting in Cloud Providers


- **AWS VPC:** By default, an AWS Virtual Private Cloud (VPC) offers 65,536 IP addresses. These addresses can be split into smaller subnets based on the CIDR notation.
    - **Example:** If you want a subnet with 256 IP addresses, you could use a CIDR block like 1.23.45.6/24, which means you have 256 IP addresses in the range 1.23.45.0 to 1.23.45.255.
    - CIDR (Classless Inter-Domain Routing) is used to specify the number of available IP addresses by indicating the number of bits dedicated to the network part of the address.
- **Private Cloud Providers:** In private cloud environments, platforms like OpenStack or Azure also support subnetting to divide resources effectively.


#### CIDR Notation and Subnet Sizes

CIDR notation uses a slash (/) followed by a number to specify the network's size, determining how many bits are used for the network portion. **For example:**

- `1.23.45.6/24` : This means 24 bits are used for the network portion, leaving 8 bits for the host addresses, which allows for 256 IP addresses in the range `1.23.45.0` to `1.23.45.255` .
- The number after the slash represents how many bits are allocated to the network portion of the IP address.

#### CIDR and Powers of 2

CIDR allows flexible subnetting based on the number of IP addresses you need:

- `/8`: A Class A IP address **(e.g., 10.0.0.0/8)**, which allows for **16,777,216** IP addresses `(2^24)`.
- `/16`: A Class B IP address **(e.g., 172.16.0.0/16)**, which allows for **65,536** IP addresses `(2^16)`.
- `/24`: A Class C IP address **(e.g., 192.168.1.0/24)**, which allows for **256** IP addresses `(2^8)`.

You can calculate the number of IP addresses in a subnet using the formula:

- `2^(32 - CIDR)` = Number of usable IP addresses.
    - **Example:** For `/24`, it would be `2^(32 - 24)` = `256` IP addresses.
    - For `/16`, it would be `2^(32 - 16)` = `65,536` IP addresses.

#### 📌  Private IP Address Ranges

- Private subnets typically use the following ranges:These ranges are reserved for use in private networks and cannot be routed on the public internet.
    - `10.0.0.0` to `10.255.255.255` **(CIDR: 10.0.0.0/8)**
    - `172.16.0.0` to `172.31.255.255` **(CIDR: 172.16.0.0/12)**
    - `192.168.0.0` to `192.168.255.255` **(CIDR: 192.168.0.0/16)**

##### Subnetting Example:

- **IP Range:** `172.16.0.0` **to** `172.16.255.255`
    - **CIDR**: `172.16.0.0/16`
    - **Total IPs:** `65,536` IP addresses.
    - This means the first 16 bits (the 172.16 part) are fixed, and the remaining 16 bits can be used for hosts.
    
The IP range for `172.16.0.0/16` will be from `172.16.0.0` to `172.16.255.255`, which gives us **65,536** possible IP addresses.


#### CIDR Notation Breakdown

- **`1.23.45.6/24` :**
    - The `/24` means the first 24 bits are fixed, and the last 8 bits (the range 0-255 in the last octet) can be assigned to hosts.
    - The network portion is `1.23.45`, and the host portion is the last octet, which can be any value from 0 to 255.
      
    ```
    Example: 1.23.45.0/24 includes IPs from 1.23.45.0 to 1.23.45.255.
    ```
### Ports

- A Port is a unique number used to direct network traffic to specific services or applications running on a device or server. Ports allow devices to handle multiple services using the same IP address but different port numbers.
    
    
    
**📌 Commonly used ports include:** 
    
    - Port 80 for HTTP (web traffic).
    - Port 443 for HTTPS (secure web traffic).
    - Port 22 for SSH (secure shell access).
    - Port 25 for SMTP (email transmission).
    
    Each service or application communicates using a specific port number, helping to direct traffic to the right service on the host.
    
---

### Prerequisite Steps Before OSI Layer



Before data travels through the **OSI (Open Systems Interconnection) model**, certain initial steps are performed to prepare the communication. These steps occur before the actual data journey begins within the OSI layers.

**1. DNS Resolution** 

![UntitledDiagram](https://github.com/user-attachments/assets/30360a65-ea32-4989-83db-dc63bd334bbb)


- **DNS (Domain Name System)**  is like a directory for the internet, where domain names are mapped to IP addresses. **For example** , when you type google.com, the system needs to find the corresponding IP address (e.g., 172.217.11.46) to connect to the Google server.
- **How DNS Works:** 
    - **Local Cache:**  The first thing that happens is the local cache is checked on your device. If you've visited the website before, the corresponding IP address might already be stored locally, so it doesn't need to be looked up again.
    - **DNS Server Check:**  If the address isn't found in the cache, the router will send a request to the DNS server (usually provided by your Internet Service Provider or ISP). This server holds a database of domain names and their corresponding IP addresses.
    - **ISP DNS:**  If the ISP's DNS does not have the record, it will query higher-level DNS servers (often using recursive resolution) until the correct IP is found.
    - **Final Response:**  Once the DNS server returns the correct IP address, it is stored locally (for faster future access) and passed back to the client.

**2. TCP Handshake** 

![a9f3c622a3b47bb86c9233fbf28b5158](https://github.com/user-attachments/assets/2eb193c4-992b-4447-a73b-8c2d9f837c1b)


- **TCP (Transmission Control Protocol)**  is a connection-oriented protocol, meaning that before sending any data, it ensures that both the client and the server are ready to communicate.
- **Three-Way Handshake:** 
    - **SYN (Synchronize):**  The client sends a SYN message to the server to initiate the connection.
    -  **SYN-ACK (Synchronize-Acknowledgment):**  The server acknowledges the request by sending back a SYN-ACK message.
    -  **ACK (Acknowledgment):**  The client sends an acknowledgment message, confirming the connection is established.
- This process ensures that both the client and server are synchronized and ready for reliable communication. Once this handshake is complete, the data transfer begins.


#### 📌 Other Types of Handshakes

- **2-Way Handshake:**  This is typically used in simpler protocols, where only a request and acknowledgment are exchanged.
- **4-Way Handshake:** Commonly seen in protocols like Wi-Fi, where additional steps are needed for security and encryption.

--- 

### OSI Model: The Journey of Data

![f-gooden_22-01_OSIModel](https://github.com/user-attachments/assets/0e65537d-e31b-4c8e-b0f0-0c16d56201c7)


The **OSI (Open Systems Interconnection)** model is a conceptual framework used to understand and standardize the processes involved in network communications. It breaks down the communication process into **7 layers**, each handling specific tasks to ensure smooth communication between devices. Below is an overview of the layers and their functions:

**╰┈➤   Layer 7 - Application Layer (User Interface and Request Identification)**

- The Application Layer is where communication begins. This is the layer that users interact with through applications such as browsers, email clients, etc.
- **Functions:** It handles the data that is intended for end-user applications. It includes request identification, like when you send an HTTP request to a website (e.g., https://google.com), passing data such as headers, authentication information, and other application-specific data.

```bash
Examples: HTTP, HTTPS, FTP, SMTP.
```

**╰┈➤  Layer 6 - Presentation Layer (Data Formatting and Encryption)**

- The Presentation Layer is responsible for translating data into a format that the receiving application can understand. This layer can also handle encryption and decryption, compression, and data encoding.
- **Functions:** It ensures that data is in a readable format for the receiving system. It may encrypt sensitive data for secure transmission (e.g., SSL/TLS for HTTPS) or convert file formats.

```bash
Examples: SSL/TLS (encryption), JPEG (image format), ASCII (text format).
```

**╰┈➤ Layer 5 - Session Layer (Session Management and Authentication)**

- The Session Layer is responsible for establishing, managing, and terminating sessions between two devices.
- **Functions:** It maintains sessions so that the application doesn’t need to authenticate multiple times. Sessions are typically stored in cookies or caches for reuse during subsequent requests, reducing the need for repeated authentication.

```bash
Examples: APIs, RPC (Remote Procedure Calls), SQL sessions.
```

```
📌 Note: The Application, Presentation, and Session Layers are typically handled by browsers and are more transparent to users.
```

**╰┈➤ Layer 4 - Transport Layer (Data Segmentation and Protocol Identification)**

- The Transport Layer ensures reliable data transfer between devices. It segments the data into smaller units (segments) and identifies which protocol to use for transport, either TCP (Transmission Control Protocol) or UDP (User Datagram Protocol).
- **Functions:** This layer handles end-to-end communication, error correction, flow control, and reliability. By default, HTTP uses TCP for reliable transmission.

```bash
Examples: TCP, UDP, SCTP.
```

**╰┈➤ Layer 3 - Network Layer (Routing and Packet Forwarding)**

- The Network Layer is responsible for making routing decisions based on the source and destination IP addresses. Routers work at this layer to direct data packets across networks, selecting the optimal path to reach the destination.
- **Functions:** It breaks data into packets and handles addressing, routing, and forwarding. This layer uses IP addressing to ensure packets are delivered to the correct destination.

```bash
Examples: IP, ICMP, routers.
```

**╰┈➤ Layer 2 - Data Link Layer (Frame Creation and MAC Address Handling)**

- The Data Link Layer is responsible for creating frames from packets and managing physical addresses (MAC addresses).
- **Functions:** It is responsible for data transfer between devices on the same network, ensuring reliable communication and error detection within the local network. Switches operate at this layer.

```bash
Examples: Ethernet, Wi-Fi, switches.
```

**╰┈➤ Layer 1 - Physical Layer (Signal Transmission and Media)**

- The Physical Layer deals with the actual physical medium that carries the data, such as cables, optical fibers, or wireless signals.
- **Functions:** This layer transmits the raw bit stream over the physical medium. It involves the conversion of data into electrical or optical signals that travel across the medium. It doesn't understand data, only electrical signals or light pulses.

```bash
Examples: Cables (Ethernet, fiber optics), wireless transmission,electrical signals,
          and network interface cards (NICs).
```
---

#### TCP/IP Model (A Simplified Version of OSI)
![image](https://github.com/user-attachments/assets/aa10e11e-b525-4d4b-a1d0-a0eeb7258d66)

The TCP/IP model is another conceptual framework, and it is more commonly used in practical networking than the OSI model. The TCP/IP model simplifies the OSI model by combining the Application, Presentation, and Session layers into a single layer called the Application Layer.

- **Layer 4 (TCP/IP):** This corresponds to the Transport Layer in the OSI model (TCP/UDP).
- **Layer 3 (TCP/IP):** This corresponds to the Internet Layer (IP).
- **Layer 2 (TCP/IP):** This corresponds to the Network Access Layer in TCP/IP, which covers the Data Link and Physical layers in OSI.

**Example of Data Flow**


1. Initiating the Request: A user types a URL (like https://google.com) in their browser. The browser uses the Application Layer to prepare the request (Layer 7).
2. Encryption: The data is then encrypted by the Presentation Layer (Layer 6) if HTTPS is used.
3. Session Management: The Session Layer (Layer 5) manages the session, checking cookies or cached data to avoid repeated authentication.
4. Segmentation: The data is divided into smaller segments by the Transport Layer (Layer 4), typically using TCP.
5. Routing: The Network Layer (Layer 3) handles the routing of these segments using the destination IP address and forwards them across the network.
6. Frame Creation: The Data Link Layer (Layer 2) creates frames, adding MAC addresses to ensure they are delivered to the right device.
7. Transmission: The Physical Layer (Layer 1) then transmits the electrical or optical signals that carry the data.

---

