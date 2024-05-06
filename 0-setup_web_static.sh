#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment

nginx_path="/etc/nginx/"
data_folder="/data"
data_static="/data/web_static/"
data_releases="/data/web_static/releases/"
data_shared="/data/web_static/shared/"
data_test="/data/web_static/releases/test/"
fake_html="/data/web_static/releases/test/index.html"
data_current="/data/web_static/current"

if [ ! -e "$nginx_path" ]; then
        sudo apt-get update
        sudo apt-get install nginx
fi
check_file() {
        local path="$1"
        if [ ! -e "$path" ]; then
                sudo mkdir -p "$path"
        fi
}
sudo chown -R "$USER:$USER" "$data_folder"
sudo find /data -type f -exec chmod +x {} \;
check_file "$data_folder"
check_file "$data_static"
check_file "$data_releases"
check_file "$data_shared"
check_file "$data_test"
echo "hello fake" | sudo tee "$(check_file "$fake_html")"
#echo "Yes fake html" | sudo tee "$fake_html"
#sudo mkdir -p "$data_test" "$data_shared"
if [ -L "$data_current" ]; then
        echo "symbolic link already exits"
        rm "$data_current"
fi
sudo ln -s "$data_test" "$data_current"

sudo sed -i '/server_name_;/a \\tlocation /hbnb_static/ {\n\t\t alias '"$data_current"';\n\t}' /etc/nginx/sites-available/default

sudo service nginx restart
exit 0
