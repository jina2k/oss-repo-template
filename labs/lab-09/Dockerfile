# Comments in Dockerfiles
FROM python:3.8.10

# Update and install dependencies
RUN apt-get update
RUN pip3 install Flask

# Set the working directory
WORKDIR /opt/webapp

COPY . .

# Set environment variables
ENV FLASK_APP=hello.py

# Expose the application's port
EXPOSE 5000

# Run the application
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
