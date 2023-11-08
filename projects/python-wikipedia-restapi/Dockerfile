FROM python:3.8.13-slim-buster

# CREATE application folder

RUN mkdir -p /application

# COPY FILES
COPY . /application

#Set working directory
WORKDIR /application

#List files and directories
RUN ls -al /application

# INSTALL DEPENDENCIES
RUN pip install -r requirements.txt

# ADDITIONAL COMMAND OF THE TEXTBLOB
RUN python -m textblob.download_corpora

# Expose instruction
EXPOSE 8080

## COMMAND TO RUN OUR APPLICATION
CMD ["python", "main.py"]
