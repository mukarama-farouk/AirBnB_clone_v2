#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""


from datetime import datetime
from fabric.api import *
import os
from os.path import exists

env.hosts = ["100.26.247.60", "100.25.29.45"]
env.user = "ubuntu"


def do_pack():
    """A function that generates a .tgz archive"""
    try:

        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")

        local("mkdir -p versions")
        src_folder = "web_static"
        archive_name = "versions/web_static_{}.tgz".format(timestamp)
        command = "tar -czvf {} {}".format(archive_name, src_folder)
        local(command)
    except Exception as e:
        None


def do_deploy(archive_path):
    """
        Distribute archive.
    """

    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        archive_filename = os.path.basename(archive_path)
        folder_name = archive_filename.split('.')[0]
        release_path = '/data/web_static/releases/{}'.format(folder_name)
        sudo('mkdir -p {}'.format(release_path))
        sudo('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_path))

        # Delete the archive from the web server
        sudo('rm /tmp/{}'.format(archive_filename))

        # Remove the current symlink
        current_path = '/data/web_static/current'
        if exists(current_path):
            sudo('rm {}'.format(current_path))

        # Create a new symbolic link to the new version
        sudo('ln -s {} {}'.format(release_path, current_path))
        print('New version deployed!')
        return True
    except Exception as e:
        return False
