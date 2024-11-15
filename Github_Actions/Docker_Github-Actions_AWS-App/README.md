# Docker_Github_Actions_AWS_App


This project demonstrates a CI/CD pipeline using GitHub Actions to build a Dockerized Python application and deploy it to an AWS EC2 instance.

## Workflow

![Streamlit -app](https://github.com/user-attachments/assets/39ad53f3-2c5c-489d-8ada-dd2af9a75d60)


1. **Code Commit**: Developers push code changes to the `main` branch.
2. **CI Build Job**: GitHub Actions triggers a build job (`build.yml`) upon code commit.
3. **Docker Image Build**: The CI job builds a Docker image from the Dockerfile and pushes it to Docker Hub upon successful build.
4. **CD Deploy Job**: After the image is pushed, another GitHub Actions job (`deploy.yml`) is triggered.
5. **Deployment to AWS EC2**:
   - The deploy job uses a self-hosted runner on an AWS EC2 instance.
   - It pulls the latest Docker image from Docker Hub.
   - The image is then run as a container on the EC2 instance.
   ![Screenshot from 2024-06-29 13-39-57](https://github.com/Raghul-M/Docker_Github-Actions_AWS-App/assets/71755586/2fc78c78-2f88-47b7-909c-d4a49a4fb220)

## Repository Structure

- **`.github/workflows/`**: Contains GitHub Actions workflows.
  - `build.yml`: Defines CI build steps.
  - `deploy.yml`: Defines CD deployment steps.
- **`Dockerfile`**: Configuration for building the Docker image.
- **`README.md`**: Project documentation (you are currently reading this file).

## Prerequisites

Before running the CI/CD pipeline, ensure you have set up the following:

- **GitHub Repository**: Configure secrets for Docker Hub credentials (`DOCKER_USERNAME`, `DOCKER_PASSWORD`) as Repo Secrets.
- **Docker Hub Account**: Repository for storing Docker images.
- **AWS EC2 Instance**: Ensure the instance is running and accessible via SSH.and Configured Self-Hosted Runner
  
![Screenshot from 2024-06-29 13-38-02](https://github.com/Raghul-M/Docker_Github-Actions_AWS-App/assets/71755586/060fa7d3-5506-4cb7-afbd-bd3c90c21936)

## Usage

1. **Fork and Clone**: Fork this repository and clone it to your local machine.
2. **Set GitHub Secrets**:
   - Navigate to your GitHub repository > Settings > Secrets.
   - Add the following secrets:
     - `DOCKER_USERNAME`: Your Docker Hub username.
     - `DOCKER_PASSWORD`: Your Docker Hub password.
4. **Configure a Self hosted Runner** : Go to Settings > Actions > Self-hosted runners.
4. **Push to `main` Branch**: Push your changes to the `main` branch to trigger the CI/CD pipeline.
5. **Monitor Execution**: View the progress of the CI/CD pipeline in the Actions tab of your GitHub repository.
6. **Verify Deployment**: Access your AWS EC2 instance to verify that the Docker container is running successfully.

## Notes

- Ensure that your Dockerfile is configured correctly to build and run your Python application.
- Regularly monitor and maintain your AWS EC2 instance to ensure proper functioning of the deployed application.

## Deployement 
![Screenshot from 2024-06-29 13-25-03](https://github.com/Raghul-M/Docker_Github-Actions_AWS-App/assets/71755586/c0cf36d7-9807-4d35-aee9-8e65c1fd4bb7)

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or want to add new features, feel free to submit a pull request.

Feel free to explore, contribute, and adapt this project to suit your needs. If you encounter any issues or have suggestions for improvement, please raise them in the GitHub repository's issues section. Happy coding! 🚀

Connect with me on linkedin: [Raghul M](https://www.linkedin.com/in/m-raghul/)

