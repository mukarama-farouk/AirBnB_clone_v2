#!/usr/bin/python3
""" Fabric script that distributes an archive to your web servers """
from fabric.api import env, run, put
import os
env.user = "ubuntu"
env.hosts = ['100.26.247.60', '100.25.29.45']

def do_deploy(archive_path):
    """
    Distribute an archive to the web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory on the server
        put(archive_path, "/tmp/")

        # Extract the archive to a temporary folder
        archive_name = os.path.basename(archive_path)
        folder_name = archive_name.split('.')[0]
        release_folder = f'/data/web_static/releases/{folder_name}'
        run(f'mkdir -p {release_folder}')
        run(f'tar -xzf /tmp/{archive_name} -C {release_folder}')
        run(f'rm /tmp/{archive_name}')

        # Move the contents to the release folder
        run(f'mv {release_folder}/web_static/* {release_folder}/')
        run(f'rm -rf {release_folder}/web_static')

        # Remove the old symbolic link
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link
        run(f'ln -s {release_folder} /data/web_static/current')

        print("New version deployed!")
        return True

    except Exception as e:
        return False
