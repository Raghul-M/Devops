import streamlit as st
from PIL import Image

# Load images
profile_pic = Image.open("profile-pic.jpg")  # Replace with your profile picture file path

# Introduction
st.title("Raghul M. - Portfolio 😀")
st.image(profile_pic, width=150)  # Display profile picture
st.subheader("Software Quality Engineer | Python Developer | DevOps Enthusiast | Founder of CareerPod")
st.write("""
Welcome to my portfolio! I'm passionate about technology, AI/ML, Cloud, and helping others grow in their careers.
""")

# Experience
st.header("Experience")

st.write("""
- **Software Quality Engineer at Red Hat**  
  Working on testing and automation in various projects, ensuring top-notch quality for products.
""")

st.write("""
- **Founder of CareerPod**  
  Leading a community to bridge the gap between students and the tech industry, offering guidance and resources.
""")

# Achievements
st.header("Achievements")
st.write("""
- **Databricks GenAI Fundamentals Certification**  
  Earned the certification in 2024, showcasing expertise in Generative AI with Databricks.
""")

st.write("""
- **Successful Deployment of Triton Model**  
  Successfully deployed a GRPC call to the Densenet model for Triton.
""")

# Volunteer Experience
st.header("Volunteer Experience")
st.write("""
- **CareerPod Volunteer Leadership**  
  Coordinated a team of volunteers to provide career guidance and tech industry insights to students.
""")

st.write("""
- **Tech Workshops and Webinars**  
  Organized and hosted several workshops and webinars to educate the community on DevOps, AI, and cloud technologies.
""")

# Skills
st.header("Skills")
st.write("""
- Python, Flask, Streamlit
- Docker, Kubernetes, AWS
- DevOps, CI/CD, GitHub Actions
- AI/ML, Data Science
- Community Building, Career Guidance
""")




# Recent Activities
st.header("Recent Activities")
st.write("""
- **Webinar on DevOps**  
  Preparing and delivering a webinar on Dockerizing a Streamlit application and deploying it using GitHub Actions.
""")

st.write("""
- **Developing Interview Preparation Tools**  
  Working on tools to generate interview questions and provide feedback based on job descriptions and candidate experience.
""")

# Certifications
st.header("Certifications")
st.write("""
- Databricks GenAI Fundamentals
""")

# Contact Information
st.header("Contact Information")
st.write("""
- LinkedIn: [linkedin.com/in/raghulm](https://www.linkedin.com/in/m-raghul/)
- GitHub: [github.com/raghulm](https://github.com/Raghul-M)
- Email: raghulmadhavan1@gmail.com
""")

# Additional Information
st.header("Additional Information")
st.write("""
- **Blog**: [Raghul's Tech Insights](https://raghul.hashnode.dev/)
- **YouTube Channel**: [CareerPod YouTube](https://youtube.com/@careerpod)
- **Twitter**: [@RaghulM01](https://x.com/RaghulM01)
""")
