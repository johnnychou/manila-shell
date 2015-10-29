#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from manilaShell.core import CoreCommand


def run():
    console = CoreCommand()
    if len(sys.argv) > 1:
        args = ' '.join(sys.argv[1:])
        console.default(args)
    else:
        console.cmdloop()

if __name__ == '__main__':
    # `python -m manilaShell` will go here.
    run()
