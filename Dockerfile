# Use official Python image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /usr/src/app

# Copy requirements
COPY requirements.txt /usr/src/app/

# Install dependencies
RUN pip install -r requirements.txt

# Copy project
COPY . /usr/src/app/

# Run the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
