#start with base image 
FROM golang:alpine

## Add Maintainer info
LABEL maintainer="Sourav Kumar"

#setup folder
RUN mkdir app
WORKDIR /app

# Copy the source from the current directory to the working Directory inside the container
COPY ./webApp /app/

# Download all the dependencies
RUN go get -d -v ./...

# Build the go app
RUN go build -o /build

# Expose port 8080 to the outside world
EXPOSE 3000

# Run the executable
CMD [ "/build" ]