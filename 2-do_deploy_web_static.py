#!/usr/bin/python3
"""A Fabric script that creates and distributes an archive to web servers
"""


from fabric.api import *
from datetime import datetime
import os

env.user = "Ubuntu"
env.hosts = ['100.26.247.60', '100.25.29.45']

def do_pack():
    """A function that generates a .tgz archive"""
    try:

        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")

        local("mkdir -p versions")
        src_folder = "web_static"
        archive_name = f"versions/web_static_{timestamp}.tgz"

        local(f"tar -czvf {archive_name} {src_folder}")
    except:
        None


def do_deploy(archive_path):
    """
        Distribute archive.
    """
    if os.path.exists(archive_path):
        archived_file = archive_path[9:]
        newest_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -xzf {} -C {}/".format(archived_file,
                                             newest_version))
        run("sudo rm {}".format(archived_file))
        run("sudo mv {}/web_static/* {}".format(newest_version,
                                                newest_version))
        run("sudo rm -rf {}/web_static".format(newest_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newest_version))

        print("New version deployed!")
        return True

    return False
