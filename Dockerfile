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
RUN pip3 install --no-cache-dir -r requirements.txt --user

# Copy the rest of the application code
COPY . /app/

EXPOSE 8501

ENTRYPOINT [ "streamlit", "run" ]

CMD ["app.py"]