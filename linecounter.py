# -*- coding: utf-8 -*-

import os
import time

class ScanCfg:
    def __init__(self, rootDir, blackList, typeFilter):
        self.rootDir = rootDir
        self.blackList = blackList
        self.typeFilter = typeFilter

class ScanResult:
    def __init__(self):
        self.linesCount = linesCount

class LineCounter:
    def scan(self, scanCfg):
        fileList = self.getFile(scanCfg)

        totalLine = 0
        for f in fileList:
            totalLine = totalLine + self.countLine(f)
        
        print (scanCfg.rootDir + " > total lines:" + str(totalLine))
        
    def countLine(self, fname):
        count = 0
        for file_line in open(fname, 'r', encoding='UTF-8', errors='ignore').readlines():
            if file_line != '' and file_line != '\n':  # 过滤掉空行
                count += 1
        #print (fname + '----', count)
        return count

    def getFile(self, scanCfg):
        filelists = []
        for parent, dirnames, filenames in os.walk(scanCfg.rootDir):
            #for dirname in dirnames:
            #    getFile(os.path.join(parent,dirname)) #递归
            for filename in filenames:
                ext = filename.split('.')[-1]
                #只统计指定的文件类型，略过一些log和cache文件
                if ext in scanCfg.typeFilter:
                    filelists.append(os.path.join(parent, filename))

        return filelists

if __name__ == '__main__' :
    cfg = {
        # 要扫描的rootDir列表，每个rootDir将会单独出一份报告
        "rootDirs": [
            r"D:\wepop_svn_analyze\S3",
            r"D:\wepop_svn_analyze\S4",
            r"D:\wepop_svn_analyze\S5",
            r"D:\wepop_svn_analyze\S6",
            r"D:\wepop_svn_analyze\S7",
            r"D:\wepop_svn_analyze\S8",
        ],
        "blackList": [],  # rootDir的相对目录
        "typeFilter": ['cs', 'lua']  # 要扫描的文件类型
    }

    counter = LineCounter()
    for root in cfg["rootDirs"]:
        scanCfg = ScanCfg(root, cfg["blackList"], cfg["typeFilter"])
        counter.scan(scanCfg)


