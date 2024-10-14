# Continuous Integration and Continuous Delivery
![64413537f97faec15d7cd2da_60d315cb607a32718b6e86c3_CICD pipelines work](https://github.com/user-attachments/assets/7508fdf0-cd3c-4792-bcc8-e6f54f48fa49)
### Continuous Integration (CI)
- **Build → Test**  
  This process involves automatically building the application and running tests every time code is committed.

### Continuous Delivery (CD)
- **Build → Test → Deploy to Staging → Deploy to Production**  
  Continuous delivery ensures that code changes are automatically prepared for a release to production, requiring manual approval before deployment.

### Continuous Deployment
- **Build → Test → Deployment (Automatic)**  
  In continuous deployment, code changes that pass all tests are automatically deployed to production without any manual intervention.

---

# Jenkins 
![Jenkins_logo_with_title svg](https://github.com/user-attachments/assets/36239b1a-a3b9-47d1-810b-d270637c6605)

Jenkins is a popular open-source CI/CD tool used to run CI/CD pipelines.

### Why Jenkins?
- **Open Source**: Free to use and modify.
- **Extensive Plugin Ecosystem**: Offers a wide range of plugins to enhance functionality.
- **Flexibility**: Can be adapted to fit various workflows and requirements.
- **Platform Agnostic**: Runs on any platform with a Java Virtual Machine (JVM).
- **Strong Community Support**: Large user community for support and resources.
- **Easy to Install and Configure**: Quick setup process.
- **Pipeline as Code**: Supports defining pipelines in code (e.g., Jenkinsfile).
- **Scalability**: Can handle a large number of jobs and users.
- **Rich Set of Tools for Monitoring and Reporting**: Provides insights into build processes.
- **Integration with Development and Deployment Tools**: Works well with other tools in the development ecosystem.

### Jenkins Helps With:
- **Manual Build and Deployment Processes**: Automates repetitive tasks.
- **Lack of Consistency**: Standardizes build processes.
- **Delayed Feedback**: Provides immediate feedback on code changes.
- **Limited Scalability**: Scales to handle more users and jobs.
- **Poor Visibility and Traceability**: Offers detailed logs and reports.
- **Difficulty in Collaborating**: Enhances team collaboration.
- **Increased Risk of Human Error**: Reduces the chance of mistakes in manual processes.
- **Resource Intensive**: Optimizes resource usage.
- **Lack of Automated Testing Integration**: Integrates testing into the CI/CD process.

---

# Jenkins Jobs

A **Jenkins job** is a set of instructions detailing what actions to perform. It provides logs for every step, allowing developers or DevOps engineers to identify and resolve errors.

### Types of Jobs:
- **Freestyle Project**: Basic job configuration (can use Groovy scripts).
- **Pipeline**: Jenkinsfile contains all the instructions for the pipeline.
- **Multi-Configuration Project**: Runs the same build with different configurations.
- **Folder**: Groups multiple projects and jobs.
- **Multi-Branch Pipelines**: Supports multiple branches in a single repository.

### Difference Between Freestyle and Pipeline Jobs
- **Freestyle Jobs**: Simpler, less flexible, and mostly suitable for straightforward tasks.
- **Pipeline Jobs**: More powerful, allows for complex workflows, and supports features like versioning through the Jenkinsfile.

---

# Jenkins Build Triggers

Build triggers define the events that will initiate a Jenkins build.

### Common Build Triggers:
- **Builds After Other Projects Are Built**: Job A triggers Job B.
- **Builds Periodically**: Schedule builds (e.g., every day at 5 PM).
- **GitHub Hook Trigger for Git SCM Polling**: Automatically triggers builds based on GitHub events.
- **Poll SCM**: Checks for changes at specified intervals and triggers builds if changes are detected.
- **Trigger Builds Remotely**: Allows external systems to trigger a Jenkins build via API.

---

# Environment Variables

Environment variables are key-value pairs used to configure and influence software running on the system. They can store credentials, secrets, and keys.

### Types of Environment Variables:
- **System Environment Variables**: Global variables like `PATH`.
- **Jenkins Environment Variables**: Specific to Jenkins jobs (e.g., `JOB_NAME`).

### Use Cases for Environment Variables:
- **Managing Credentials**: Securely store sensitive information.
- **Configuring Builds**: Customize build behavior.
- **Customizing Behavior**: Change how jobs execute based on variable values.

### Jenkins Built-in Environment Variables:
- `BUILD_ID`: Unique ID for the build.
- `BUILD_NUMBER`: Incrementing build number.
- `BUILD_TAG`: Combination of job name and build number.
- `BUILD_URL`: URL to access the build.
- `EXECUTOR_NUMBER`: Number of the executor running the build.
- `JAVA_HOME`: Path to the JDK.
- `JENKINS_URL`: URL of the Jenkins instance.
- `JOB_NAME`: Name of the job.
- `NODE_NAME`: Name of the node executing the job (e.g., `master`).
- `WORKSPACE`: Absolute path to the job's workspace.

---

# Credentials Management

Jenkins provides a secure way to store and handle sensitive data such as credentials, API tokens, SSH keys, and SSL certificates.

### Credential Scope:
- **Global**: Available to all jobs and pipelines.
- **System**: Limited to specific domains.
- **User**: Unique to the user, typically used for personal access.

---

# Pipeline Stages: Nested and Parallel Examples


### Example of Nested Stages

In this example, we demonstrate how to create nested stages within a pipeline. This allows you to logically group related steps under a parent stage.

```groovy
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
                // Simulate build step
                sh 'echo "Build completed!"'
            }
            stages {
                stage('Compile') {
                    steps {
                        echo 'Compiling source code...'
                        // Simulate compile step
                        sh 'echo "Compilation completed!"'
                    }
                }
                stage('Package') {
                    steps {
                        echo 'Packaging the application...'
                        // Simulate package step
                        sh 'echo "Packaging completed!"'
                    }
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                // Simulate test step
                sh 'echo "Tests completed!"'
            }
        }
    }
}
```

### Example of Parallel Stages

In this example, we demonstrate how to run multiple stages in parallel. This is useful for executing tasks that can be done simultaneously, which can significantly speed up the build process.

```groovy
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
                // Simulate build step
                sh 'echo "Build completed!"'
            }
        }
        stage('Test') {
            parallel {
                stage('Unit Tests') {
                    steps {
                        echo 'Running unit tests...'
                        // Simulate unit test step
                        sh 'echo "Unit tests completed!"'
                    }
                }
                stage('Integration Tests') {
                    steps {
                        echo 'Running integration tests...'
                        // Simulate integration test step
                        sh 'echo "Integration tests completed!"'
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                // Simulate deployment step
                sh 'echo "Deployment completed!"'
            }
        }
    }
}
```

### Summary

- **Nested Stages**: Used to logically group steps under a parent stage, providing better organization and clarity in the pipeline structure.
- **Parallel Stages**: Used to execute multiple tasks simultaneously, improving efficiency and reducing overall pipeline execution time.


### Pipeline Options
- **timeout**: Define a maximum duration for a stage.
- **skipDefaultCheckout**: Skip the default checkout of source code.
- **retry**: Retry a stage if it fails.

### Parameters
You can define parameters in your pipeline for dynamic inputs. Example:

```groovy
pipeline {
    agent any
    parameters {
        string(name: 'VERSION', defaultValue: '1.0', description: 'Version of the application')
    }
    stages {
        stage('Build') {
            steps {
                echo "Building version: ${params.VERSION}"
            }
        }
    }
}
```


### Jenkins Pipeline with Input

```groovy
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
                sh 'echo "Build completed!"'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'echo "Tests completed!"'
            }
        }
        stage('Approval') {
            steps {
                script {
                    def userInput = input(
                        id: 'UserInput', 
                        message: 'Do you want to proceed with deployment?', 
                        parameters: [[$class: 'BooleanParameterDefinition', name: 'Proceed', defaultValue: true]]
                    )
                    echo "User input received: ${userInput}"
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                sh 'echo "Deployment completed!"'
            }
        }
    }
}
```

### Key Points:
- **Approval Stage**: Uses `input` to prompt the user for confirmation before deployment.
- **Parameters**: A Boolean parameter allows the user to approve or cancel the deployment.
- **Flow**: If approved, the pipeline proceeds to the deployment stage.

This structure helps ensure that critical actions, like deploying to production, are manually confirmed.
