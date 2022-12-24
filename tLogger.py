# coding: UTF-8
from __future__ import print_function
import datetime as dt
import linecache
import logging
import os


class Logger(object):
    @staticmethod
    def wLog(content, fileName, recordGrade=0, mode="a", precision=2):
        """
        2022/10/9/20:26
        :param content: 日志内容
        :param fileName: 日志名
        :param recordGrade: 日志记录等级
        :param mode: 日志写入模式
        :param precision: 精细度
        :return prs: The program running state 程序运行状态
        """
        # noinspection PyBroadException
        try:
            iod = precision

            # 写入时间
            nowTime = dt.datetime.now().strftime('%Y-%m-%d$%H-%M-%S-%f')
            pelFile = open(fileName, mode)
            pelFile.write(nowTime)
            pelFile.close()  # 关闭文件
            # 写入日志内容
            if iod == 1:
                ldc = '|%(name)s-%(levelname)s-%(message)s'
            elif iod == 2:
                ldc = '|%(name)s-%(levelname)s-%(message)s|%(threadName)s-%(thread)d$%(processName)s-%(process)d'
            elif iod == 3:
                # 精细度最高
                ldc = "|%(name)s-%(levelname)s-%(message)s|%(threadName)s-%(thread)d$%(processName)s-%(process)d|%(" \
                      "pathname)s-%(funcName)s "
            else:
                # 默认 ldc
                ldc = "|%(name)s-%(levelname)s-%(message)s|%(threadName)s-%(thread)d$%(processName)s-%(process)d"

            logging.basicConfig(filename=fileName, level=logging.DEBUG, format=ldc)

            log = logging.getLogger(__name__)
            # 写入 content
            if recordGrade == 0:
                log.debug(content)
                return 0  # 返回
            elif recordGrade == 1:
                log.info(content)
                return 0  # 返回
            elif recordGrade == 2:
                log.warning(content)
                return 0  # 返回
            elif recordGrade == 3:
                log.error(content)
                return 0  # 返回
            elif recordGrade == 4:
                log.critical(content)
                return 0  # 返回
            else:
                log.info(content)
        except:
            return 1

    @staticmethod
    def rLog(nosl, file, TailLine, delimiter="/"):
        """
        不想写，不想写，不想写，不想写，不想写，不想写。
        :param nosl: 分割成度
        :param file: Log文件
        :param TailLine: 行数
        :param delimiter: 分隔符
        :return:
        """
        TotalLine = len(open(file, "r").readlines())
        fileContent = linecache.getline(file, TotalLine + 1 - TailLine)
        if nosl == 1:
            return delimiter.join(fileContent.split("|"))
        elif nosl == 2:
            splitTemp = delimiter.join(fileContent.split("|"))
            return delimiter.join(splitTemp.split("$"))
        elif nosl == 3:
            splitTemp = delimiter.join(delimiter.join(fileContent.split("|")).split("$"))
            return delimiter.join(splitTemp.split("-"))

    @staticmethod
    def clog(fileName) -> None:
        """
        Clean up excess log files
        :param fileName: 文件名
        :return: None
        """
        os.system('del /F /S /Q ' + fileName)
