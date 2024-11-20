## **Introduction**

![image](https://github.com/user-attachments/assets/0b2b0cc2-1340-4684-9c73-09b9cc8d2f0c)


**Linux**:

- An open-source operating system that acts as an intermediary between software and hardware.

### **Unix vs Linux**

**Unix**:

- Developed in Bell Laboratories in the 1970s.
- **Purpose:** Multi-user and multi-tasking.
- **Commercial versions:** Solaris (Sun Microsystems), AIX (IBM), HP-UX (Hewlett-Packard).
- Limited file system support.

**Linux**:

- Developed by Linus Torvalds in the 1990s.
- Open-source and modifiable.
- **Popular distributions:** RedHat, Debian, CentOS.
- Used in ATMs, smartphones, home appliances, video game consoles.

**Uses of Linux**

- TVs
- Home appliances
- Smartphones
- Video game consoles
- ATM machines

---

### **Virtualization**

![image](https://github.com/user-attachments/assets/8ac3fde3-7cd0-41c2-91a8-890cc2e2f628)


**VirtualBox**:

- Developed by Oracle.
- Allows running multiple operating systems on a single hardware.

**Example**:

- **Host:** Windows 10
- **Guest OS:** Windows 7, Ubuntu, MacOS

**Virtual Machine**:

- An imaginary computer with no need for physical hardware.

---



**📌 Key Concepts: Restaurant Example**

- **Operating System (OS)**: The entire restaurant (includes the kitchen, dining area, staff, and management).
- **Kernel**: The kitchen (where the actual food preparation happens, handling raw ingredients).
- **Linux**: A specific type of restaurant (e.g., an Italian restaurant with a specific style and menu).
- **Terminal**: The waiter (takes orders from customers and communicates them to the kitchen).


---

**Important things in linux:**

1. **Root** - super user account, - create,edit & delete account, - change configurations, - delete entire OS.
2. case sensitive system
3. avoid spaces when creating files or directories for easly file access.
4. Linux kernel is not an OS: - It is a small software, Takes command from users passess to the hardware or peripherals.
5. Linux mostly used with CLI not with GUI.

---

### **Snapshots**

- A point-in-time copy of a system's state.
- Used for storage, virtual machines, or databases.
- Enables quick restoration or rollback if needed.
- It allows you to capture the state of a system or data at a specific moment, enabling quick restoration or rollback if needed.
- If anything happened like os crashes we don’t need to reinstall the os. if we snapshot we can use that.
  
---

### **Essential Commands**

1. **General:**
    - `ip addr` or `ifconfig`: Show IP address.
    - `whoami`: Shows the current user.
    - `su <username>`: Switch between users.
    - `hostname`: Prints the hostname.
2. **System Information**:
    - `man <cmd>`: Manual pages for the command.
    - `clear`: Clears the terminal screen.
    - `passwd`: Change the password.
    - `passwd <user>`: Change password for other users (root only).
3. **File System Navigation**:
    - `cd`: Change directory.
    - `pwd`: Print working directory.
    - `ls`: List directory contents.
    - `mkdir <dir>`: Create a directory.
    - `rmdir <dir>`: Remove a directory.
    - `rm <file>`: Remove a file.
4. **File Operations**:
    - `touch <filename>`: Create a new file.
    - `cp <source> <destination>`: Copy a file.
    - `mv <source> <destination>`: Move or rename a file.
    - `rm <filename>`: Remove a file.
    - `cat <filename>`: Display file content.
    - `head <filename>`: Display the first lines of a file.
    - `tail <filename>`: Display the last lines of a file.
    - `find <path> -name <filename>`: Find files.
    - `grep <pattern> <file>`: Search for a pattern in a file.
5. **Process Management**:
    - `ps`: List running processes.
    - `top`: Real-time process monitoring.
    - `kill <PID>`: Stop a process.
6. **Disk Management**:
    - `df -h`: Display disk space usage.
    - `du -h`: Display disk usage.

---

### **Filesystem Structure**

![image](https://github.com/user-attachments/assets/2cc141e1-a49b-492e-a422-ba33b960910b)


**Filesystem :** a system used by os to manage files. It controls how data saved and retrieved (like your closet)

**Different types of filesystems** : ext3,ext4,xfs,[linux] NFTS, FAT[Windows] etc..

```
📌 Overview of Filesystem :

-  /bin : User-level commands.
-  /sbin : System-level commands.
-  /etc : Configuration files.
-  /dev : Device files.
-  /proc : Process information.
-  /var : System logs.
-  /tmp : Temporary files.
-  /usr : User programs and commands.
-  /home : User directories.
-  /boot : Bootloader files.
-  /lib : Library files.
-  /opt : Optional add-on applications.
-  /mnt : Mount removable media manually.
-  /media : Mount external hard drives, flash drives, CD-ROMs.
-  /srv : Site-specific data (ftp, www).
```

---

 **Navigating the File System**

- **Absolute Path**:
    - Example: `cd /usr/bin` (specifies the full path)
    - Takes you directly to the specified directory from the root directory.
- **Relative Path**:
    - Example: `cd Documents` (specifies the directory or file name relative to the current location)
    - Takes you to a directory or file relative to your current location.
- **Going Back One Folder**:
    - Use `cd ..` to move up one directory level.
    - Useful for navigating back to the parent directory.

---

### **Links**

Its like making a virtual copy of a physical data. In linux we have two types of links

**Hard Links**:

- Direct pointers to the same file data.

**Symbolic Links**:

- Pointers to the path of the target file.

**Inodes**:

- Crucial for managing files and directories in a filesystem.
- Store important metadata about files.
- Actual filenames are stored in directory entries that map to these inodes.
- Inode acts as a unique identification number for files and folders.

**Symbolic Link**:
  - Functions like creating a shortcut for a file in Windows.
  - Only points to the data file; no content is shared.
  - Created using the command:
    
    ```bash
    $ ln -s <sourcefile> <symbolicfilename>.
    ```
    
**Hard Link**:
  - Directly contains the data from the shared file.
  - If one changes, another one also changes.
  - Both share the same file size and inode number.
  - Created using the command:
    
    ```bash
    $ ln <sourcefile> <hardlinkfilename>.
    ```
    
**Viewing Inode Number**:
  - Use `$ ls -i *data_file` to show the inode number of a file

---

### **Understanding File/Folder Permissions:**

The permissions `-rw-rw-r--` indicate the following:

 - Permissions for the file owner: `rw-` (read and write)
 - Permissions for group members: `rw-` (read and write)
 - Permissions for everyone else: `r--` (read only)

**Where:**

- `r`: Read permission
- `w`: Write permission
- `x`: Execute permission (for binary files or executables)

**Changing File/Folder Permissions:**

- `chmod`: Change mode
    - `u`: User
    - `g`: Group
    - `o`: Others
    - `a`: All
    - `-` : Remove permission
    - `+`: Add permission

Example:

- `$ chmod u-w <filename>`: Removes write permission for the user.

**Changing Ownership:**

- `$ chown <userneeded_to_change> <filename>`: Changes the user ownership of a file.
- `$ chown <.groupname> <filename>`: Changes the group ownership of a file.
- `$ chown <user .group> <filename>`: Changes ownership for both user and group simultaneously.

**To Add  a user in sudo file**

In the file last add <username> ALL=(ALL)  ALL  (It enables the sudo access for the user )

```bash
$ vi sudo
```

---

### **Package Management**

![image](https://github.com/user-attachments/assets/2cfc9fdd-a7cc-4ed2-a3be-ea89c51bf68b)


**Debian-based (Ubuntu, Linux Mint)**:

- `dpkg`, `apt`

**RedHat-based (CentOS, Fedora)**:

- `yum`, `rpm`

```bash
$ yum list installed - It list all the yum via installed packages.
$ yum list <package name> - show package info
$ yum install zip
$ yum remove zip
```

---

### **Users and Groups**

**Users**:

1. Create user: `adduser <username>`
2. Set password: `passwd <username>`
3. Delete user: `userdel -r <username>`
4. Lock user: `passwd -l <username>`
5. Unlock user: `passwd -u <username>`

**Groups**:

1. Create group: `groupadd <groupname>`
2. List groups: `cat /etc/group`
3. Modify group: `groupmod -g <GID> <groupname>`
4. Delete group: `groupdel <groupname>`
5. Add user to group: `usermod -aG <groupname> <username>`
6. List user groups: `groups <username>`
7. List group users: `getent group <groupname>`
8. Remove user from group: `gpasswd -d <username> <groupname>`

---

### **Other Commands**

```bash
$ less       # View the content of a file one screen at a time
$ man        # Display the manual pages for a command
$ uname      # Print system information (e.g., kernel name, version)
$ tar        # Archive files (tar) and extract files from an archive (tar -x)
$ cmp        # Compare two files byte by byte
$ service    # Start, stop, or restart a system service
$ traceroute # Show the route packets take to a network host
$ ufw        # Firewall management tool
$ wget       # Download files from the web
$ iptables   # Configure IPv4 packet filtering rules in the Linux kernel
$ cal        # Display a calendar in the terminal
$ alias      # Create a shortcut for a command
$ whereis    # Locate the binary, source, and manual page files for a command
$ whatis     # Display a brief description of a command
$ useradd    # Create a new user
$ usermod    # Modify a user account
$ passwd     # Change a user password

## Sorting Data

$ sort <filename>: It sorts the data in the file in alphabetical order.
$ sort file.txt -n: Sorts data numerically.
$ sort filename -M: Sorts data by month.
$ sort filename -Mr: Sorts data by month in reverse order.

## Grep - Global Regular Expression Print (Searching Data)

$ grep <content/word> <filename>: Searches for content or a word in a file.
$ grep <content/word> -c <filename>: Returns the count of occurrences of content/word in a file.
$ grep -e <word1> -e <word2> <filename>: Searches for multiple words in a file.
$ grep -E '<regex exp>' <filename>: Searches for patterns using regular expressions.

## Compress Data

## Gzip - GNU Zip

   $ gzip <filename>: Compresses data.
   $ gzip -d <compressedfile.gz>: Decompresses the compressed file.
   $ gzip -c <filename> > foo.gz: Compresses and renames the compressed file.

```

---

### **Environment Variables**


1. **Global Variables**
2. **Local Variables**

**Commands:**

- `$ printenv`: Shows all global environment variables in the system.
- `$ echo <$ENV_VARIABLE>`: Prints the value of a specific environment variable.

**Local Variables:**

- `$ MYVAR=1234`: Defines a local variable. To print its value, use `$ echo $MYVAR`. Note that local variables are lost once the terminal is closed.
- `$ unset <local var_name>`: Unsets a local variable.

**Setting a Global Variable:**

- Global variables can be set in the `.bashrc` file.

---

### **Command Prompt**

![image](https://github.com/user-attachments/assets/bc06af1f-3e01-4267-adc2-7d5cb0713dfa)


The Command Prompt is a command-line interface (CLI) program in operating systems. It allows users to execute commands to perform various tasks such as navigating the file system, managing files and directories, running scripts, and configuring system settings. It provides a text-based way to interact with the OS

```bash
user@hostname~ $
```

- `$`: Normal user
- `#`: Root user

---
