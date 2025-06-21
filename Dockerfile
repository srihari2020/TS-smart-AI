# Use official Python 3.10 image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy all files from local to container
COPY . .

# Upgrade pip and install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port (update if you're using another port)
EXPOSE 5000

# Start the app (change app.py if your main file has a different name)
CMD ["python", "app.py"]

