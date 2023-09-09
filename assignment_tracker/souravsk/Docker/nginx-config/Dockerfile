#using base image nginx 
FROM nginx:latest

# Copy your SSL certificate and private key to the container
COPY nginx.crt /etc/nginx/nginx.crt
COPY nginx.key /etc/nginx/nginx.key

# Copy your Nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Expose ports (HTTP and HTTPS)
EXPOSE 80
EXPOSE 443

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]