#!/usr/bin/python3
"""Create and distributes an archive to web servers"""
import os.path
import time
from fabric.api import local
from fabric.operations import env, put, run

env.hosts = ['100.26.247.60', '100.25.29.45']


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

    except:
        None


def do_deploy(archive_path):
    """Distribute an archive to web servers"""
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        file = archive_path.split("/")[-1]
        folder = ("/data/web_static/releases/" + file.split(".")[0])
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(folder))
        run("tar -xzf /tmp/{} -C {}".format(file, folder))
        run("rm /tmp/{}".format(file))
        run("mv {}/web_static/* {}/".format(folder, folder))
        run("rm -rf {}/web_static".format(folder))
        run('rm -rf /data/web_static/current')
        run("ln -s {} /data/web_static/current".format(folder))
        print("Deployment done")
        return True
    except:
        return False


def deploy():
    """Create and distributes an archive to web servers"""
    try:
        path = do_pack()
        return do_deploy(path)
    except:
        return False
