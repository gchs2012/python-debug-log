#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import Debug as debug

reload(sys)
sys.setdefaultencoding('utf-8')

debug_log = debug.Debug("test.log", True)


def test():
    log_msg = "%s test example." % debug.comm_get_func_head_info()
    debug_log.debug_write_log(log_msg)

    string = "test"
    log_msg = "%s test example. %s" % (debug.comm_get_func_head_info(), string)
    debug_log.debug_write_log(log_msg)


if __name__ == '__main__':
    test()
