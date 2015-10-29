#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import cmd
import sys
import regex as re

from manilaShell import constants
from manilaShell.lib import log
from manilaShell.lib import execute

LOG = log.getLogger(__name__)


class CoreCommand(cmd.Cmd, object):

    def __init__(self):
        super(CoreCommand, self).__init__()
        # The prompt issued to solicit input.
        self.prompt = '=> '

    def _get_command(self, cmd):
        for key, command in self.commands.iteritems():
            if (key == cmd):
                return command
        else:
            print("Not Such Command!!!")

    def do_exit(self, args):
        """Exits from the console"""
        return sys.exit(1)

    def do_EOF(self, args):
        return self.do_exit(args)

    def do_man(self, args):
        LOG.info('do_man command [%s].', args)

    def do_help(self, args):
        LOG.info('do_help command [%s].', args)

    # Override methods in Cmd object ##
    def preloop(self):
        """Initialization before prompting user for commands.

        Despite the claims in the Cmd documentaion,
        Cmd.preloop() is not a stub.
        """
        super(CoreCommand, self).preloop()   # sets up command completion

    def postloop(self):
        """Take care of any unfinished business.

        Despite the claims in the Cmd documentaion,
        Cmd.postloop() is not a stub.
        """
        super(CoreCommand, self).postloop()   # Clean up command completion

    def precmd(self, line):
        """
        This method is called after the line has been input but before
        it has been interpreted. If you want to modifdy the input line
        before execution (for example, variable substitution) do it here.
        """
        return line

    def postcmd(self, stop, line):
        """If you want to stop the console, return something that evaluates to true.

        If you want to do some post command processing, do it here.
        """
        return stop

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def cmdloop(self, intro=None):
        while True:
            try:
                super(CoreCommand, self).cmdloop(intro)
                self.postloop()
                break
            except KeyboardInterrupt:
                print("^C")

    def default(self, line):
        """Called on an input line when the command prefix is not recognized.

        In that case we execute the line as Python code.
        """
        LOG.info('default command [%s] enter.', line)

        match = re.match(constants.exp, line)
        if match:
            ret = execute.gluster_exec(match.group(0))
            print(ret)
            LOG.info('default command [%s] Result [%s].', line, ret)
