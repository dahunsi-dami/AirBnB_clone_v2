#!/usr/bin/python3
"""
Fabric script to generate .tgz archive
from contents of web_static folder.
"""

from fabric.api import *
from datetime import datetime
from os import path


def do_pack():
    """
    do_pack generates .tgz archive w/ web_static content.
    """

    # Create `versions` folder if it doesn't exist already.
    local('sudo mkdir -p versions')

    try:
        # Create archive with name format:
        time = datetime.now().strftime('%Y%m%d%H%M%S')
        local(f'sudo tar -cvzf versions/web_static_{time}.tgz web_static')

        # Get size of newly created .tgz archive.
        filepath = f"versions/web_static_{time}.tgz"
        filesize = path.getsize(filepath)
        print(f"web_static packed: {filepath} -> {filesize}Bytes")
    except Exception as e:
        return None
