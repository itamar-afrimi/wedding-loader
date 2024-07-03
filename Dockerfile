FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the service account key JSON file into the container
COPY wedding-uploader-412016-5f9a11ebbdac.json .
# Copy the application code
COPY . .

ENV GOOGLE_APPLICATION_CREDENTIALS=wedding-uploader-412016-5f9a11ebbdac.json
# Expose the port the app runs on
EXPOSE 8080

# Run the application
CMD ["gunicorn", "-b", ":8080", "app:app"]
