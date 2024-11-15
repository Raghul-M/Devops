# Deploying_Docker-App-on-Render_Using_Githubactions



# Streamlit Portfolio Application
![Streamlit -app (1)](https://github.com/user-attachments/assets/a2e2a7e5-cf9d-4dc8-bb85-001ddf8685d6)



This repository contains the code for a Streamlit-based portfolio application, which has been dockerized and is deployed on Render using GitHub Actions. The project showcases how to build, containerize, and deploy a Streamlit application seamlessly using Docker and automated CI/CD pipelines.



## Running the Application Locally

To run the Streamlit application locally, use the following command:

```bash
streamlit run app.py
```

This command will start the Streamlit server and open your application in a web browser.

## Building and Running with Docker

### 1. Log in to Docker Hub

Before building the Docker image, you need to log in to Docker Hub. Replace `<username>` with your Docker Hub username:

```bash
docker login -u <username>
```

### 2. Build the Docker Image

Build the Docker image using the Dockerfile in the root of the repository. Replace `<username>` with your Docker Hub username:

```bash
docker build -t <username>/streamlit-portfolio:v1 .
```

This command will create a Docker image tagged with `v1`.

### 3. Verify Docker Images

List all Docker images on your local machine to ensure that the build was successful:

```bash
docker images
```

### 4. Run the Docker Container

Run the Docker container using the image you built. This command will map port `8051` on your local machine to port `8051` in the container. Replace `<username>` with your Docker Hub username:

```bash
docker run -d --name portfolio -p 8051:8051 <username>/streamlit-portfolio:v1
```

The application should now be accessible at `http://localhost:8051`.

### 5. Push the Docker Image to Docker Hub

Finally, push the Docker image to Docker Hub to make it available for deployment. Replace `<username>` with your Docker Hub username:

```bash
docker push <username>/streamlit-portfolio:v1
```


## Deployment

The Docker image can be deployed to various platforms, such as Render, AWS, or any other cloud provider that supports Docker containers.

![Screenshot from 2024-08-20 23-23-32](https://github.com/user-attachments/assets/34d3105a-3ffa-49f2-9915-ba2bf985f606)

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or want to add new features, feel free to submit a pull request.

Feel free to explore, contribute, and adapt this project to suit your needs. If you encounter any issues or have suggestions for improvement, please raise them in the GitHub repository's issues section. Happy coding! 🚀

Connect with me on linkedin: [Raghul M](https://www.linkedin.com/in/m-raghul/)
