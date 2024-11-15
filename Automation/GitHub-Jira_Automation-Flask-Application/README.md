# GitHub-Jira Automation Flask Web Application

![Jira automation](https://miro.medium.com/v2/resize:fit:1400/1*hzETdS_uSTlDKZienV0xTA.png)
## Overview
This GitHub-Jira integration project involves a Flask web application hosted on an AWS EC2 instance. The application automates the creation of Jira issues based on GitHub issue comments. Specifically, when a user comments "/jira" on a GitHub issue, the web application triggers a process that utilizes GitHub webhooks, Jira API automation, and AWS EC2.

## How It Works

1. **GitHub Webhooks:**
     [![Screenshot-from-2023-12-16-01-18-43.png](https://i.postimg.cc/c42SWNcx/Screenshot-from-2023-12-16-01-18-43.png)](https://postimg.cc/1fGT02T2)
   - The Flask web application is configured to receive GitHub webhook events.
   - GitHub issues trigger events that contain information about comments, which the application analyzes.

3. **GitHub Issue Comment Processing:**
   [![Screenshot-from-2023-12-16-01-25-34.png](https://i.postimg.cc/qMwdt307/Screenshot-from-2023-12-16-01-25-34.png)](https://postimg.cc/SJnP3jn0)
   - When a comment is made on a GitHub issue, the application checks if it contains the "/jira" command.

5. **Jira API Automation:**
     [![Screenshot-from-2023-12-16-01-20-57.png](https://i.postimg.cc/C11PdRFW/Screenshot-from-2023-12-16-01-20-57.png)](https://postimg.cc/PLgzRrv4)
   - If the "/jira" command is detected, the application uses the Jira REST API to create a new issue on the Jira board.
   - Key details such as project, issue type, and summary are included in the API request payload.

6. **AWS EC2 Hosting:**
   - The Flask web application is hosted on an AWS EC2 instance.
   - Ensure you have launched an EC2 instance, and you can access it securely.

7. **Setup After Creating EC2 Instance:**
   - Connect to your EC2 instance securely using SSH.
   - Run these commands :
     ```bash 
        $ sudo apt-get update
        $ sudo apt-get install python3
        $ sudo apt-get install python3-pip
        $ pip install flask
        $ vim your-filename.py
        $ python3 your-filename.py
     ```
     [![Screenshot-from-2023-12-16-01-23-53.png](https://i.postimg.cc/15k3HF2r/Screenshot-from-2023-12-16-01-23-53.png)](https://postimg.cc/Wh7Vpd2d)
     - It will initiate the Flask application

# Troubleshooting Guide

## Problem:
[![Screenshot-from-2023-12-16-01-32-10.png](https://i.postimg.cc/cC3WNWr5/Screenshot-from-2023-12-16-01-32-10.png)](https://postimg.cc/Fkh8j2bj)
Webhooks are failing, or the Flask application returns a 500 error.

## Possible Causes and Solutions:

1. **Webhooks Configuration:**
   - Verify GitHub webhook settings (payload URL, content type, and secret).

2. **Flask Application Logs:**
   - Check application logs for errors (commonly in `/var/log` or the app directory).

3. **EC2 Security Groups:**
   - Go to EC2 console > Security Groups.
   - Ensure Inbound Rules allow necessary ports (e.g., 80, 443 , 5000) for GitHub IPs.

## Reference Screenshot:
[![Screenshot-from-2023-12-16-01-27-15.png](https://i.postimg.cc/HsTsrHGT/Screenshot-from-2023-12-16-01-27-15.png)](https://postimg.cc/s10RLkDL)



Feel free to explore, contribute, and adapt this project to suit your needs. If you encounter any issues or have suggestions for improvement, please raise them in the GitHub repository's issues section. Happy coding! 🚀

