#!/usr/bin/env python
import os
import sys

from subprocess import Popen



if __name__ == "__main__":
    Popen(["python", "instabot.py/example.py"])
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
