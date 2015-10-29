#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shlex
import subprocess


def gluster_exec(command):
    args = shlex.split(command)
    gluster = subprocess.Popen(
        args,
        shell=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

    return gluster.stdout.read()
