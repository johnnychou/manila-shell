#!/usr/bin/env python
# -*- coding: utf-8 -*-

STATUS = {
    'SYS_SUCCESSFUL': 'SYS_SUCCESSFUL',
    'SYS_FAILED': 'SYS_FAILED',
    'CMD_INCOMPLETE': 'CMD_INCOMPLETE',
    'CMD_NO_REQUIRED_PARM': 'CMD_NO_REQUIRED_PARM',
    'CMD_UNKNOWN_PARAM': 'CMD_UNKNOWN_PARAM',
    'CMD_INVALID_PARAM': 'CMD_INVALID_PARAM',
    'CMD_UNKNOWN': 'CMD_UNKNOWN',
}

# Regular Expressions
volumeSetExp = '(set)(\s)+(\S)+(\s)+(\S)+(\s)+(\S)+'
volumeResetExp = '(reset)(\s)+(\S)+(\s)*(\S)*(\s)*(force)?'
volumeInfoExp = '(info)(\s)*(\S)*(\s)*(--xml)?'
volumeStartExp = '(start)(\s)+(\S)+(\s)*(force)?'
volumeStopExp = '(stop)(\s)+(\S)+(\s)*(force)?'
volumeQuotaExpSub1 = '(((enable)|(disable)|((list)(-objects)?))((\s)+(\S)+)*)'
volumeQuotaExpSub2 = '(((remove)|(remove-objects))(\s)+(\S)+)'
volumeQuotaExpSub3 = '((default-soft-limit)(\s)+(\S)+)'
volumeQuotaExpSub4 = '((limit-usage)(\s)+(\S)+(\s)+(\S)+(\s)*(\S)*)'
volumeQuotaExpSub5 = '((limit-objects)(\s)+(\S)+(\s)+(\S)+(\s)*(\S)*)'
volumeQuotaExpSub6 = '(((alert-time)|(soft-timeout)|(hard-timeout))(\s)+(\S)+)'
volumeQuotaExp = ('(quota)(\s)*(%s|%s|%s|%s|%s|%s)', (
    volumeQuotaExpSub1, volumeQuotaExpSub2, volumeQuotaExpSub3,
    volumeQuotaExpSub4, volumeQuotaExpSub5, volumeQuotaExpSub6))
volumeListExp = '(list)'

snapshotListExp = '(list)(\s)*(\S)*'
snapshotActivateExp = '(activate)(\s)+(\S)+(\s)*(force)?'
snapshotCloneExp = '(list)(\s)+(\S)+(\s)+(\S)+'

volumeExp = ('(volume)(\s)*(%s|%s|%s|%s|%s|%s|%s)' % (
    volumeSetExp, volumeResetExp, volumeInfoExp, volumeStartExp,
    volumeStopExp, volumeQuotaExp, volumeListExp))
snapshotExp = ('(volume)(\s)*(%s|%s|%s)' % (
    snapshotListExp, snapshotActivateExp, snapshotCloneExp))

exp = (r'^(gluster)(\s)*(%s|%s|--version)(\s)*$' % (volumeExp, snapshotExp))
