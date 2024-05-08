#!/usr/bin/python3
"""
Distributes an archive to your web servers
using the function do_deploy.
"""

from fabric.api import *
from datetime import datetime
from os import path

env.hosts = ["54.89.109.98", "3.89.155.105"]


def do_deploy(archive_path):
    """
    Distributes archive to web servers.

    Args:
        archive_path: path to the archive to be distributed.
    Returns:
        False if file at archive_path doesn't exist, else True.
    """

    try:
        # Check if file at archive_path exists
        if path.isfile(archive_path):
            pass
        else:
            return False

        # Upload archive to /tmp/ directory of web server
        put(archive_path, '/tmp/')

        # Create folder that'll store uncompressed archive.
        filename = archive_path.split("/")[-1].split(".")[0]
        run(f'sudo mkdir -p /data/web_static/releases/web_static_{filename}/')

        # Uncompress archive to created folder
        run(f'sudo tar -xzf /tmp/{filename}.tgz -C \
        /data/web_static/releases/web_static_{filename}/')

        # Delete the archive from the server
        run(f'sudo rm /tmp/web_static_{filename}.tgz')

        # Move files from web_static to parent folder
        run(f'sudo mv /data/web_static/releases/web_static_{filename}\
        /web_static/* /data/web_static/releases/web_static_{filename}/')

        # Remove web_static folder
        run(f'sudo rm -rf /data/web_static/releases/web_static_{filename}\
        /web_static/')

        # Delete symbolic link /data/web_static/current from web server
        run('sudo rm -rf /data/web_static/current')

        # Create new symbolic link /data/web_static/current on web server
        run(f'sudo ln -s /data/web_static/releases/web_static_{filename}/ \
            /data/web_static/current')
    except Exception as e:
        return False

    return True
