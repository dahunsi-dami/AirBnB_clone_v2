#!/usr/bin/env bash
# Set up web servers for deployment of web_static

# Update the server.
sudo apt-get update

# Install Nginx with auto yes to all prompts.
sudo apt-get -y install nginx

# Allow incoming connections through SSH, port 80, and 443.
sudo ufw allow 'OpenSSH'
sudo ufw allow 'Nginx HTTP'
sudo ufw allow 'Nginx HTTPS'

# Create /data/web_static/releases/test/ as needed.
sudo mkdir -p /data/web_static/releases/test/

# Create /data/web_static/shared.
sudo mkdir -p /data/web_static/shared/

# Create index.html file in test directory.
sudo touch /data/web_static/releases/test/index.html

# Recursively assign ownership of data to user running script.
sudo chown -R ubuntu:ubuntu /data/

# Set permissions of files in /data to rwx for user, r-x for g:o.
sudo chmod -R 755 /data/

# Create fake content for index.html.
sudo echo "<html>
  <head>
  </head>
  </body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create symbolic link /data/web_static/current
# to /data/web_static/releases/text/
sudo ln -sf /data/web_static/releases/text/ /data/web_static/current

# Serve content of /data/web_static/current/ to hbnb_static
# using alias.
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart Nginx after configuration.
sudo service nginx restart
