#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
******************************************************************************

            Copyright (C) 2017-2018, xxx Co.xxx, Ltd.

******************************************************************************
    File : Debug.py
    Auth : zc
    Date : 2018/8/29/
    Desc : debug log
******************************************************************************
"""
import os
import sys
import time
import datetime
reload(sys)
sys.setdefaultencoding('utf-8')


""" get current time
"""
def comm_get_cur_time():
    try:
        cur_time = time.strftime("%Y/%m/%d %X", time.localtime())
    except:
        # 2016/1/1 00:00:00
        cur_time = "2016/1/1 00:00:00"
    return cur_time


""" get current time stamp
"""
def comm_get_cur_time_stamp():
    try:
        cur = time.localtime()
        date = datetime.datetime(cur.tm_year, cur.tm_mon, cur.tm_mday,
                                 cur.tm_hour, cur.tm_min, cur.tm_sec)
        timestamp = int(time.mktime(date.timetuple()))
    except:
        # 2016/1/1 00:00:00
        timestamp = 1451577600
    return timestamp


""" get function name
"""
def comm_get_func_head_info():
    try:
        raise Exception
    except:
        f = sys.exc_info()[2].tb_frame.f_back
        return "[%s:%s]" % (f.f_code.co_name, str(f.f_lineno))


""" get file size
"""
def comm_get_file_size(file_path):
    try:
        size = os.path.getsize(file_path)
    except Exception, e:
        print("[%s]%s File `%s` is not exists! ErrCode = %s!\n" %
              (comm_get_cur_time(), comm_get_func_head_info(), file_path, e))
        size = 0
    return size


""" Debug class
"""
class Debug:
    __log_file_size_hash__ = {'5MB': 5242880,
                              '10MB': 10485760,
                              '15MB': 15728640,
                              '20MB': 20971520,
                              '25MB': 26214400,
                              '30MB': 31457280}
    __log_switch__ = False
    __log_file__ = "DebugLog.log"

    def __init__(self, log_file="DebugLog.log", log_switch=False):
        self.__log_file__ = log_file
        self.__log_switch__ = log_switch
        try:
            open(self.__log_file__, "a").write("")
        except Exception, e:
            print("[%s]%s Open `%s` file or write log data failed! ErrCode = %s!\n" %
                  (comm_get_cur_time(), comm_get_func_head_info(), self.__log_file__, e))

    # set debug switch
    def debug_set_switch(self, log_switch):
        self.__log_switch__ = log_switch

    # write log file
    def debug_write_log(self, log_msg):
        log = "[%s]%s\n" % (comm_get_cur_time(), log_msg)
        try:
            if self.__log_switch__ is True:
                if comm_get_file_size(self.__log_file__) > self.__log_file_size_hash__['30MB']:
                    open(self.__log_file__, "w").write(log)
                else:
                    open(self.__log_file__, "a").write(log)
            print(log)
        except Exception, e:
            print("[%s]%s Open `%s` file or write log data failed! ErrCode = %s!" %
                  (comm_get_cur_time(), comm_get_func_head_info(), self.__log_file__, e))
