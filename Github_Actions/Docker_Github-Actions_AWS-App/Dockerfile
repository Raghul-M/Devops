FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y 
    
COPY . .

RUN pip3 install -r requirements.txt

ENV GOOGLE_API_KEY=""

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501"]
