#!/usr/bin/python3
""" A Fabric script that generates a .tgz archive from the contents of the web_static folder 
"""


from fabric.api import local
from datetime import datetime

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

if __name__ == '__main__':
    do_pack()
