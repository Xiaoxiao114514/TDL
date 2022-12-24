# coding: UTF-8
from __future__ import print_function
import zipfile
import os


class Tzip(object):
    global zcv

    @staticmethod
    def anZip(testDir, fileName, uzpw=b"<>{];/. Un <>{];/. Zip /*-+ PassWord *498`+-*/1"):
        with zipfile.ZipFile(fileName, 'w') as z:
            for d in os.listdir(testDir):
                z.setpassword(uzpw)
                z.write(d)
                z.close()

    @staticmethod
    def unZip(testDir, fileName, uzpw=b"<>{];/. Un <>{];/. Zip /*-+ PassWord *498`+-*/1"):
        with zipfile.ZipFile(fileName, 'r') as z:
            z.extractall(testDir, pwd=uzpw)

    @staticmethod
    def readZip(fileName):
        with zipfile.ZipFile(fileName, 'r') as z:
            files = z.namelist()
            print(files)
