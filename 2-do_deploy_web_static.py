#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""

from datetime import datetime
from fabric.api import *
import os

env.hosts = ["44.210.150.159", "35.173.47.15"]
env.user = "ubuntu"


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
        run("mkdir -p {}".format(newest_version))
        run("tar -xzf {} -C {}/".format(archived_file,
                                             newest_version))
        run("rm {}".format(archived_file))
        run("mv {}/web_static/* {}".format(newest_version,
                                                newest_version))
        run("rm -rf {}/web_static".format(newest_version))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(newest_version))

        print("New version deployed!")
        return True

    return False
