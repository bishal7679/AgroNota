# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# add user (change to whatever you want)
# prevents running sudo commands
RUN useradd -r -s /bin/bash bishal

# set current env
ENV HOME /app
WORKDIR /app
ENV PATH="/app/.local/bin:${PATH}"

RUN chown -R bishal:bishal /app
USER bishal

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt --user

# Copy the rest of the application code
COPY . /app/

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the application
CMD ["python", "main.py"]
