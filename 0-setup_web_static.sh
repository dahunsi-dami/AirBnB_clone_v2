#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment

nginx_path="/etc/nginx"
data_folder="/data"
data_static="/data/web_static"
data_releases="/data/web_static/releases"
data_shared="/data/web_static/shared"
data_test="/data/web_static/releases/test"
fake_html="/data/web_static/releases/test/index.html"
data_current="/data/web_static/current"

if [ ! -e "$nginx_path" ]; then
        sudo apt-get update
        sudo apt-get install -y nginx
fi
check_file() {
        local path="$1"
        if [ ! -e "$path" ]; then
                sudo mkdir -p "$path"
        fi
}
sudo chown -R ubuntu:ubuntu "$data_folder"
sudo find "$data_folder" -type f -exec chmod +x {} \;
check_file "$data_folder"
check_file "$data_static"
check_file "$data_releases"
check_file "$data_shared"
check_file "$data_test"
html_content='<html>
        <head>
        </head>
        <body>
                Holberton School
        </body>
</html>'
echo "$html_content" | sudo tee "$fake_html"
#echo "Yes fake html" | sudo tee "$fake_html"
#sudo mkdir -p "$data_test" "$data_shared"
#if [ -L "$data_current" ]; then
        #echo "symbolic link already exits"
        #sudo rm "$data_current"
#fi
sudo ln -sf "$data_test" "$data_current"

sudo sed -i '/server_name_;/a \\tlocation /hbnb_static/ {\n\t\t alias '"$data_current"';\n\t}' /etc/nginx/sites-available/default

sudo nginx -s reload
exit 0
