# Use an official lightweight Python image.
FROM python:3.9-slim

# Set environment variables.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /flask-onion

# Install dependencies.
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the local code to the container's workspace.
COPY . /flask-onion

# Run the application on the internal network at port 8000.
EXPOSE 8000
CMD ["gunicorn", "--config", "./deploy/flask/gunicorn-config.py", "run:app"]
