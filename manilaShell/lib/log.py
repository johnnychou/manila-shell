#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

log_level = logging.DEBUG

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler = logging.FileHandler('manila-shell.log')
handler.setLevel(log_level)
handler.setFormatter(formatter)


def getLogger(name):
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    logger.addHandler(handler)
    return logger
